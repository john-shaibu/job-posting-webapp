
from enum import Flag
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
      id = db.Column(db.Integer, primary_key=True, autoincrement=True)
      firstname = db.Column(db.String(60), nullable = False)
      lastname = db.Column(db.String(60), nullable = False)
      age = db.Column(db.Integer)
      phone_number = db.Column(db.String(30), nullable=False, unique=True)
      email = db.Column(db.String(60), nullable=False, unique=True)
      password = db.Column(db.String(60), nullable=False)
      is_recruiter = db.Column(db.Boolean, nullable=False, default=False)

      def __repr__(self):
            return f"User('{self.firstname}', '{self.lastname}')"

class Recruiter(db.Model):
      id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
      recruiter_id = db.Column(db.Integer, primary_key=True)
      company_name = db.Column(db.String(120), nullable=False)
      is_company = db.Column(db.Boolean, nullable=False)
      company_category = db.Column(db.String(60), nullable=False)
      company_sub_category = db.Column(db.String(60), nullable=False)
      recruiter_email = db.Column(db.String(60), db.ForeignKey('user.email'), nullable=False)
      bio = db.Column(db.String(250))
      no_of_employee = db.Column(db.Integer)
      jobs = db.relationship('Job', backref='author', lazy=True)

      def __repr__(self):
            return f"Recruiter('{self.id}')"

class Comment(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
      job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
      user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
      comment = db.Column(db.String(600), nullable=False)

      def __repr__(self):
            return f"Comment('{self.id}', '{self.date_posted}', '{self.comment}')"

class Job(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      job_title = db.Column(db.String(120), nullable=False)
      hiring_multiple = db.Column(db.Boolean, nullable=False, default=False)
      date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
      job_role = db.Column(db.Text, nullable=False, default='Job role not specified')
      job_requirements = db.Column(db.Text, nullable = False, default='Job requirements not speified')      
      full_job_description = db.Column(db.Text, nullable=False, default= 'Job description not specified')
      salary = db.Column(db.String(50), nullable=False, default='Not Specified')
      salary_type = db.Column(db.String(30), nullable=False)
      job_type = db.Column(db.String(60), nullable=False)
      author_id = db.Column(db.Integer, db.ForeignKey('recruiter.id'), nullable=False)
      job_deadline = db.Column(db.DateTime, nullable=False, default='Not Specified')
      
      def __repr__(self):
            return f"Job('{self.job_title}', '{self.date_posted}', '{self.author_id}')"