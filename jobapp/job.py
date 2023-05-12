from flask import (
      Blueprint, flash, g, redirect, render_template, request, url_for,session
)
from werkzeug.exceptions import abort

from jobapp.auth import login_required
# from jobapp.models import get_db

bp = Blueprint('job', __name__)

from .models import User, db

@bp.route('/')
def index():
      
      return render_template('job/home.html')

@bp.route('/job/')
def job_page():


      return render_template('job/job.html')


@bp.route('/user/<int:id>')
def profile_page(id):

      # id = session.get('user_id')
      user_info = User.query.filter_by(id=id)


      return render_template('job/user_profile.html')