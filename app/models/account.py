""" This module contains necessary data for each account"""
from app.models.user import User
class Account(object):
    """Account Class that contains stored details of a specific account in bucketbook"""
    #pylint: disable-msg=R0913
    def __init__(self, username, email, password):
        """ initializes the credentials of user"""
        self.username = username
        self.email = email
        self.password = password
    #pylint: disable-msg=R0913
    def get_account_credentials(self,username, email, password):
        """ checks validation of user to register """
        credentials = User(
            username=username,
            email=email,
            password=password,)
        return credentials 
    def login_account(self, email, username, password):
        """ checks validation of user to login """
        login_credentials = User(
            username=username,
            email=email,
            password=password,)
        return login_credentials
    