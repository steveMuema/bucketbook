""" This modules contain routes for handling application pages """
from functools import wraps
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from app import app
from app.controller import RegisterForm, CreateBucket, LoginForm
from passlib.hash import sha256_crypt
from bucket_data import Buckets
from app.models.user import User
from app.models.store import Stores
from app.models.bucketlist import Bucketlist

sampleBuckets=Buckets()
app.users= {}
app.bucketlist={}
app.activities={}
app.secret_key="df74e77b964ea"
@app.route('/')
def index():
    """ Starting page of the application containing brief description of the app"""
    return render_template("getting-started.html")

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if  'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/register', methods=['GET', 'POST'])
def register():
    """ opens register page and validates user form"""
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        new_user = [email, username, password]
        new_user=User(email, username, password).save_credentials
        app.users[username]= new_user
        print("You're now registered please login", 'success', app.users)
        return redirect(url_for('login'))
    return render_template("register.html", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    """ open the login page"""
    form=LoginForm()
    if request.method=="POST":
        # Get Form Fields
        username = request.form['username']
        password_candidate = sha256_crypt.encrypt(str(form.password.data))
        user = [username, password_candidate]
        session['logged_in'] = True
        session['email'] = Stores.account_store
        if password_candidate == Stores.account_store[2]:
            print("You're successfully logged in.", user)
            return redirect(url_for('bucketlist'))
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template("login.html")
 
 #Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


@app.route('/bucketlists')
@is_logged_in
def bucketlist():
    """ opens the bucketlists page. Home page of application """
    return render_template("bucketlists.html")

# @app.route('/home', methods=['POST'])
# def addlist():
#     if request.method=='POST':
#         bucket = form.addlist.data
#         print(bucket)
# @app.route()

@app.route('/add_buckets', methods=['GET', 'POST'])
@is_logged_in
def add_buckets():
    form = CreateBucket(request.form)
    if request.method == 'POST' and form.validate():
        bucketname= form.bucketlist.data
        bucket_id=request.form['bucket_id']
        bucket=Bucketlist(bucketname, bucket_id).save_bucketlist
        app.bucketlist[bucket_id]=bucket
    return render_template("bucketlists.html", bucket=app.bucketlist)
    
@app.route('/bucket')
def view_bucket(bucket):
    if request.method=="POST":
         return redirect(url_for('bucketlist'))
    else:
        bucket=Bucketlist.get_buckets
        return render_template("bucketlist.html", bucket=bucket)


@app.route('/activities')
def activities():
    """ opens the activities page"""
    return render_template("activities.html")
@app.route('/about')
def about():
    """ opens the about page"""
    return render_template("about.html")

