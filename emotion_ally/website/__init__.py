from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'a32192bc-5866-4e53-ba25-4da273ba8fe0' # encrypt session data

  # import and register blueprints views
  from .views import views

  app.register_blueprint(views, url_prefix='/') 

  return app