""" bucketbook initialization with my configs.
"""
from flask import Flask
# #load the views
from app import views


#initialize the app
APP = Flask(__name__, instance_relative_config=True)




#load config file
APP.config.from_object('config')
