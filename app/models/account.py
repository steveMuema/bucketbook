""" This module contains necessary data for each account"""
from app.models.bucketlist import Bucketlist
from app.models.activities import Activities
from app.models.register import Register
class Account(object):
    """Account Class that contains stored details of a specific account in bucketbook"""
    #pylint: disable-msg=R0913
    def __init__(self, firstname, lastname, email, password, index, buckets, buckets_activities):
        """ initializes the credentials of user"""
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.index = index
        self.buckets = [buckets]
        self.buckets_activities = [buckets_activities]
    #pylint: disable-msg=R0913
    def get_account_credentials(self, firstname, lastname, email, password, index):
        """ inherits attributes from register"""
        credentials = Register(
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=password,
            index=index,
        )
        return credentials 
    def set_bucketlist(self):
        """sets bucketlist to account and returns the list created"""
        bucketlist = Bucketlist.get_buckets(self)
        return bucketlist
    def create_activity(self, buckets_activities):
        """inherits from bucketlist"""
        buckets_activities = Activities(
            buckets_activities=buckets_activities
        )
        return buckets_activities
