""" This module contains necessary data for each account"""
from app.models.bucketlist import Bucketlist
from app.models.activities import Activities
from app.models.register import Register
class Account(object):
    """Account Class that contains stored details of a specific account in bucketbook"""
    def __init__(self, firstname, lastname, email, password, index, txtbucket, activitytxt):
        """ initializes the credentials of user"""
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.index = index
        self.txtbucket = txtbucket
        self.activitytxt = activitytxt

    def account_credentials(self, firstname, lastname, email, password, index):
        """ inherits attributes from register"""
        credentials = Register(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            index=index,
        )
        return credentials 
    def create_bucketlist(self, txtbucket):
        """inherits from bucketlist"""
        bucketlist = Bucketlist(
            txtbucket=txtbucket
        )
        return bucketlist
    def create_activity(self, activitytxt):
        """inherits from bucketlist"""
        activity = Activities(
            activitytxt=activitytxt
        )
        return activity
