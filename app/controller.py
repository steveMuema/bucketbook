from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length

class RegisterForm(FlaskForm):
    """ form that handles lregistration"""
    username =  StringField('username', validators=[InputRequired(), Length(min=4, max=25)])
    email = StringField('email', validators=[InputRequired(), Email(message="Invalid address"), Length(min=5, max=25)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=25)])

class LoginForm(FlaskForm):
    """ form that handles login"""
    username =  StringField('username', validators=[InputRequired(), Length(min=4, max=25)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=25)])

class CreateBucket(FlaskForm):
    """ handles new buckets created"""    
    buckets_name = StringField('buckets_name', validators=[InputRequired(), Length(min=4, max=140)])

class CreateActivity(FlaskForm):
    """ used to create new activity"""
    activitytxt = StringField('activitytxt', validators=[InputRequired(), Length(min=4, max=140)])
    # buckets_name = StringField('Buckets_name', validators=[InputRequired(), Length(min=4, max=140)])

class EditBucket(FlaskForm):
    """  edits available buckets """
    buckets_name = StringField('buckets_name')
    new_buckets_name = StringField('buckets_name', validators=[InputRequired(), Length(min=4, max=140)])

class EditActivity(FlaskForm):
    """ edits available activity"""
    activitytxt = StringField('activitytxt')
    new_activitytxt = StringField('activitytxt', validators=[InputRequired(), Length(min=4, max=140)])

class RemoveBucket(StringField):
    """ removes a deleted bucket"""
    buckets_name = StringField('buckets_name')

class RemoveActivitytxt(StringField):
    activitytxt = StringField('activitytxt')
