
from ast import Try
import functools
import pyotp
from flask import (
      Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from jobapp.models import db, User

bp = Blueprint('auth', __name__, url_prefix='/auth')


#============================================================================
def generate_otp():
      totp = pyotp.TOTP('base32secret3232',interval=400)
      otp=totp.now() 

      return totp,otp
#USER REGISTER VIEW
@bp.route('/register', methods = ('GET', 'POST'))
def register():

      global user_to_create
      global generated_otp, totp

      # db = get_db()

      if request.method == 'POST':
            error = None
            phone_number = request.form['phone']

            if phone_number.startswith('0'):
                  phone_number = '+234' + phone_number[1:]

            fullname = request.form['fullname']
            firstname = fullname.split()[0]
            lastname = fullname.split()[1]

            user_to_create = {
                  'firstname' : firstname,
                  'lastname' : lastname,
                  'email' : request.form['email'],
                  'phone_number' : phone_number
            }
            
            if not user_to_create['email']:
                  error = 'An email is required.'

            elif not fullname:
                  error = 'Pls provide a name.'

            elif User.query.filter_by(email = user_to_create['email']).first() is not None:
                  error = 'user already registered'

            # elif not user_to_create['phone_number']:
            #       error = 'A phone number is required.'

            if error is None:
                  totp,generated_otp = generate_otp()
                  print(generated_otp)
 
                  print(user_to_create)
                  return redirect(url_for('auth.verification'))

            flash(error)

      return render_template('auth/userregister.html')

@bp.route('/verification', methods = ('GET', 'POST'))
def verification():

      if request.method == 'POST':
            error = None
            entered_otp = int(request.form['otp'])
            print(entered_otp)
            verify = totp.verify(entered_otp)
            if verify == False:

                  error = 'Invalid otp.'
            else:
                  print('otp verified!!!')
                  return redirect(url_for('auth.password'))

            flash(error)

      return render_template('auth/validation.html', email=user_to_create['email'])


@bp.route('/password', methods = ('GET', 'POST'))
def password():
      # db = get_db
      error = None
      if request.method == 'POST':
            password1 = request.form['password1']
            password2 = request.form['password2']

            if not password1: 
                  error = 'A password is required.'

            elif not password2: 
                  error = 'A confirmation password is required.'

            elif password1 !=  password2:
                  error = 'Password mismatch.'

            if error is None:
                  print(password1, password2)

                  user_to_create['password'] = generate_password_hash(password1)

                  print(user_to_create)

                  try:
                        u = User(
                              firstname = user_to_create['firstname'],
                              lastname = user_to_create['lastname'],
                              phone_number = user_to_create['phone_number'],
                              email = user_to_create['email'],
                              password = user_to_create['password']                 
                        )

                        db.session.add(u)
                        db.session.commit()

                        print('Account created!!!')

                        return redirect(url_for('auth.login'))
                  except:
                        error = 'Error creating account. Try again!!!'

            flash(error)

      return render_template('auth/password.html')

# USER LOGIN VIEW
@bp.route('/login', methods = ('GET', 'POST'))
def login():
      if request.method == 'POST':
            error = None
            email = request.form['email']
            password = request.form['password']

            if not email:
                  error = 'An email is required.'
            elif not password:
                  error = 'An password is required.'

            user = User.query.filter_by(email = email).first()

            print(user)

            if user is None:
                  print('invalid login credentials!!')
                  error = 'Invalid email'

            elif not check_password_hash(user.password, password):
                  error = 'Incorrect password.'

            if error is None:
                  print(email, password)
                  session.clear()
                  session['user_id'] = user.id

                  # print(session['user_id'])

                  return redirect(url_for('job.index'))

            flash(error)

      return render_template('auth/userlogin.html')


#===============================================================================

# RECRUITER REGISTER VIEW
@bp.route('/register-recruiter', methods = ('GET', 'POST'))
def register_recruiter():
      

      return render_template('auth/recruiterlogin.html')

# RECRUITER LOGIN VIEW
@bp.route('/recruiter-login', methods = ('GET', 'POST'))
def login_recruiter():
      

      return render_template('auth/recruiterlogin.html')

@bp.route('/logout-recruiter', methods = ('GET', 'POST'))
def logout_recruiter():
      session.clear()
      return redirect(url_for('login_recruiter'))

#================================================================================

# registers a funcrion that runs before the view function 
#checks if a user id is stored in the session and gets theh user's data fro the database
@bp.before_app_request
def load_logged_in_user():
      user_id = session.get('user_id')
      # print(user_id)
      if user_id is None:
            g.user = None
      else:
            g.user = User.query.filter_by(id = user_id).first()
            print(g.user)


# registers a funcrion that runs before the view function 
#checks if a recruiter id is stored in the session and gets theh recruiter's data fro the database
# @bp.before_app_request
# def load_logged_in_recruiter():
#       recruiter_id = session.get('user_id')
#       if recruiter_id is None:
#             g.recruiter = None
#       else:
#             g.recruiter = get_db().execute(
#                   'SELECT * FROM recruiter WHERE id = ?', (recruiter_id,)
#             ).fetchone()


# this decorator returns a new view function thatt wraps the original view it's applied to.
# The new function checks iif a user is loaded and redirects to the login page otherwise..
def login_required(view):
      @functools.wraps(view)
      def wrapped_view(**kwargs):
            user_id = session.get('user_id')
            user = User.query.filter_by(id = user_id).first()
            if user is None:

                  return redirect(url_for('auth.login'))

            return view(**kwargs)

      return wrapped_view

@bp.route('/logout')
def logout():
      session.clear()
      return redirect(url_for('auth.login'))