from app.models.store import Stores
class Bucketlist(object):
    def __init__(self, txtbucket):
        self.txtbucket = txtbucket


    """ creates new bucketlist and appends to the store with save_bucketlist"""
    def bucketlist_stores(self):
        """return information to be called  when appending to the store for bucketlist[bucketlist_store]"""
        return{'txtbucket': self.txtbucket}

    @classmethod
    def new_bucketlist(self, txtbucket):
        """ sets the attribute of the class to new_bucketlist and calls save_bucketlist() to append on store"""
        new_bucketlist=self(txtbucket)
        new_bucketlist.save_bucketlist()

    def save_bucketlist(self):
        """ method for appending created txtbucket to the bucketlist_store on (central) store   """
        Stores.bucketlist_store.append(self.bucketlist_stores())
