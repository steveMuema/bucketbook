"""" use this to configure the @app/route paths in the html files """
from app import app
from flask import Flask, flash, redirect, render_template, request, session, abort


@app.route('/')
def index():
    """ navigates to the root page index.html """
    if not session.get('logged in'):
        return render_template("signin.html")
    return render_template("home.html")


@app.route('/signup')
def signup():
    """ navigates to the signup page signup.html """
    return render_template("signup.html")


@app.route('/signin', methods=['GET', 'POST'])
def do_login():
    """ navigates to the sign page signin.html """
    if request.form['email'] == 'hitchs3x@gmail.com' and request.form['username'] == 'hitch' and request.form['password']=='say123#':
        session['loggedin']=True
    else:flash('Authenticaion error, Try again')
    return render_template("home.html")


@app.route('/home')
def home():
    """ navigates to the home page home.html """
    return render_template("home.html")


@app.route('/home/activities')
def activities():
    """ navigates to the activites page activities.html """
    return render_template("activities.html")