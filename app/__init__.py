""" bucketbook initialization with my configs.
"""
from flask import Flask



#initialize the app
APP = Flask(__name__, instance_relative_config=True)

# #load the views
from app import views

#load config file
APP.config.from_object('config')
