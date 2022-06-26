# store main URL endpoints for front-end; roots (pages not for auth)

from flask import Blueprint, flash, render_template, request

# for rendering templates
# set up blueprint 
views = Blueprint('views', __name__)

# create routes (links to each page) and render html
@views.route('/', methods=['GET', 'POST']) # define view # not sure if post permission is needed
def home():   
  return render_template("home.html") # return to home page and render note

@views.route('/about')
def about():
  return render_template("about.html")

@views.route('/identify', methods=['GET', 'POST'])
def user_input():
  return render_template("identify.html", description="description")

@views.route('/result')
def result():
  return render_template("result.html")

@views.route('/resources')
def resources():
  return render_template("resources.html")

@views.route('/guess-again')
def guess_again():
  return render_template("guessAgain.html")

@views.route('/login', methods=['GET', 'POST'])
def login():
  return render_template("login.html")
