import os

from flask import Flask


def create_app():
      app = Flask(__name__)

      app.config['SECRET_KEY'] = '1fe8ffb4549dd16d642b829b93868e1a'
      app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobapp.db'
      app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
      
      from jobapp.models import db
      db.init_app(app)

      with app.app_context():
            db.create_all()

      #register the authentication blueprint from auth.py to our factory
      from . import auth
      app.register_blueprint(auth.bp)

      #register the job blueprint from job.py to our factory
      from . import job
      app.register_blueprint(job.bp)
      app.add_url_rule('/', endpoint='index')

      #register the recruiter blueprint from job.py to our factory
      from . import recruiter
      app.register_blueprint(recruiter.bp)

      return app