"""" use this to configure the @app/route paths in the html files """
from flask import render_template
from app import APP


@APP.route('/')
def index():
    """ navigates to the root page index.html """
    return render_template("index.html")


@APP.route('/signup')
def signup():
    """ navigates to the signup page signup.html """
    return render_template("signup.html")


@APP.route('/signin')
def signin():
    """ navigates to the sign page signin.html """
    return render_template("signin.html")


@APP.route('/home')
def home():
    """ navigates to the home page home.html """
    return render_template("home.html")


@APP.route('/home/activities')
def activities():
    """ navigates to the activites page activities.html """
    return render_template("activities.html")
