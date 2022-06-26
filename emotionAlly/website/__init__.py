from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'lfhasdjfhdasjfhdsa' # encrypt session data

  # import and register blueprints views
  from .views import views

  app.register_blueprint(views, url_prefix='/') 

  return app