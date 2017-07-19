from app.models.store import Stores
"""Module creates, updates and deletes bucketlists from model"""
class Bucketlist(object):
    """ class will call methods new_bucketlist, read_bucketlist, delete_bucketlist, and update to account"""
    def __init__(self, txtbucket):
        self.txtbucket = txtbucket
    def bucketlist_stores(self):
        """return information to be called  when appending to the store """
        return{'txtbucket': self.txtbucket}

    @classmethod
    def new_bucketlist(cls, txtbucket):
        """ sets the attribute of the class to new_bucketlist and calls save_bucketlist()"""
        new_bucketlist = cls(txtbucket)
        new_bucketlist.save_bucketlist()

    def save_bucketlist(self):
        """ method for appending created txtbucket to the bucketlist_store on (central) store   """
        Stores.bucketlist_store.append(self.bucketlist_stores())
