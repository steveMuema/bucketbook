""" This modules contain routes for handling application pages """
from flask import render_template
from app import app
@app.route('/')
def index():
    """ Starting page of the application containing brief description of the app"""
    return render_template("getting-started.html")

@app.route('/register')
def register():
    """ opens the register page"""
    return render_template("register.html")

@app.route('/login')
def login():
    """ open the login page"""
    return render_template("login.html")

@app.route('/bucketlists')
def bucketlist():
    """ opens the bucketlists page. Home page of application """
    return render_template("bucketlists.html")

@app.route('/activities')
def activities():
    """ opens the activities page"""
    return render_template("activities.html")
@app.route('/about')
def about():
    """ opens the about page"""
    return render_template("about.html")