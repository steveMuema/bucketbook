""" This modules contain routes for handling application pages """
from functools import wraps
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from app import app
from app.controller import RegisterForm, CreateBucket, LoginForm
from passlib.hash import sha256_crypt
from app.models.user import User
from app.models.store import Stores
from app.models.bucketlist import Bucketlist


app.users= {}
app.bucketlist={}
app.activities={}
app.secret_key="df74e77b964ea"
@app.route('/')
def index():
    """ Starting page of the application containing brief description of the app"""
    return render_template("getting-started.html")

# Check if user logged in
def is_logged_in(param):
    @wraps(param)
    def wrap(*args, **kwargs):
        if  'logged_in' in session:
            return param(*args, **kwargs)
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
        
        print("You're successfully logged in.", user)
        return redirect(url_for('home'))
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


# @app.route('/bucketlists', methods=['GET', 'POST'])
# @is_logged_in
# def bucketlists():
#     """ opens the bucketlists page. Home page of application """
#     if request.method == 'POST':
#         bucketname= request.form["bucketname"]
#         bucket=Bucketlist(bucketname)
#         app.bucketlist[bucket.bucket_id] = bucket
#         return render_template("bucketlists.html", bucketlist=app.bucketlist)
#     return render_template("bucketlists.html", bucketlist=app.bucketlist)

@app.route('/editbucket/<bucket_id>', methods=['GET', 'POST'])
@is_logged_in
def edit_buckets(bucket_id):
    if request.method=='POST':
        bucketname= request.form["bucketname"]
        bucket=Bucketlist(bucketname)
        app.bucketlist[bucket.bucket_id] = bucket
        bucket.bucketname=bucketname
        return render_template('editbucketlist.html', bucketlist=app.bucketlist)
    return render_template("bucketlists.html", bucketlist=app.bucketlist)
    
@app.route('/deletebucket/<bucket_id>')
@is_logged_in
def delete_bucket(bucket_id):
    print(app.bucketlist)
    del app.bucketlist[bucket_id]
    return redirect(url_for('bucketlists'))

@app.route('/activities', methods=['GET'])
@is_logged_in
def add_activity():
    return render_template('old-activities.html')

@app.route('/home', methods=['GET', 'POST'])
@is_logged_in
def home():
    """ opens the bucketlists page. Home page of application """
    if request.method == 'POST':
        bucketname= request.form["bucketname"]
        bucket=Bucketlist(bucketname)
        app.bucketlist[bucket.bucket_id] = bucket
        return render_template("home.html", bucketlist=app.bucketlist)
    return render_template("home.html", bucketlist=app.bucketlist)


@app.route('/about')
def about():
    """ opens the about page"""
    return render_template("about.html")
