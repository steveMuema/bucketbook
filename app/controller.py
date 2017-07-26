from functools import wraps
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, IntegerField
from passlib.hash import sha256_crypt
from wtforms.validators import InputRequired, Email, Length

class RegisterForm(Form):
    """ form that handles lregistration"""
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')
class LoginForm(Form):
    """ form that handles login"""
    user_id = IntegerField('user_id')
    username =  StringField('username', validators=[InputRequired(), Length(min=4, max=25)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=25)])

class CreateBucket(Form):
    """ handles new buckets created"""    
    buckets_name = StringField('buckets_name', validators=[InputRequired(), Length(min=4, max=140)])

class CreateActivity(Form):
    """ used to create new activity"""
    activitytxt = StringField('activitytxt', validators=[InputRequired(), Length(min=4, max=140)])
    # buckets_name = StringField('Buckets_name', validators=[InputRequired(), Length(min=4, max=140)])

class EditBucket(Form):
    """  edits available buckets """
    buckets_name = StringField('buckets_name')
    new_buckets_name = StringField('buckets_name', validators=[InputRequired(), Length(min=4, max=140)])

class EditActivity(Form):
    """ edits available activity"""
    activitytxt = StringField('activitytxt')
    new_activitytxt = StringField('activitytxt', validators=[InputRequired(), Length(min=4, max=140)])

class RemoveBucket(Form):
    """ removes a deleted bucket"""
    buckets_name = StringField('buckets_name')

class RemoveActivitytxt(Form):
    activitytxt = StringField('activitytxt')
