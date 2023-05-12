
from flask import (
      Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from jobapp.auth import login_required


bp = Blueprint('recruiter', __name__, url_prefix='/recruiter')


@bp.route('/')
def dashboard():

      return render_template('recruiter/dashboard.html')

@bp.route('/p', methods=('GET', 'POST'))
def post_job():

      if request.method == 'POST':
            
            return redirect(url_for('recruiter.job_role'))

      return render_template('recruiter/basic_info.html')

@bp.route('/p/role', methods=('GET', 'POST'))
def job_role():

      if request.method == 'POST':
            
            return redirect(url_for('recruiter.job_requirement'))

      return render_template('recruiter/job_role.html')

@bp.route('/p/requirement', methods=('GET', 'POST'))
def job_requirement():

      if request.method == 'POST':
            
            return redirect(url_for('recruiter.job_description'))

      return render_template('recruiter/job_requirement.html')

@bp.route('/p/description', methods=('GET', 'POST'))
def job_description():

      if request.method == 'POST':
            
            return redirect(url_for('recruiter.job_compensation'))

      return render_template('recruiter/job_description.html')

@bp.route('/p/compensation', methods=('GET', 'POST'))
def job_compensation():

      if request.method == 'POST':
            
            return redirect(url_for('recruiter.job_preference'))

      return render_template('recruiter/job_compensation.html')

@bp.route('/p/preference', methods=('GET', 'POST'))
def job_preference():

      return render_template('recruiter/job_preference.html')

@bp.route('/username')
def recruiter_profile():


      return render_template('recruiter/recruiter_profile.html')