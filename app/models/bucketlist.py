"""This module contains fundamentals of the bucketlists class 
Attributes: buckets 'used to instantiate a bucketlist and also save value to store',
buckets_index 'returns the index of particular index'  """
from app.models.store import Stores
class Bucketlist(object):
    """ class will contain fundamentals for bucketlists"""
    def __init__(self, bucketname, bucket_id):
        """ initiate list of  buckets and add empty list of activities to a new bucket"""
        self.bucketname = bucketname
        self.bucket_id = bucket_id
    def bucketlist_stores(self):
        """return information to be called  when appending to the store """
        return{'bucketname': self.bucketname,
               'bucket_id': self.bucket_id,}
    @classmethod
    def create_bucketlist(cls, bucketname, bucket_id):
        """ method for creating new bucketlist and save to central store """
        new_bucketlist = cls(bucketname, bucket_id)
        new_bucketlist.save_bucketlist()
    def save_bucketlist(self):
        """ method for appending created buckets to the buckets_store on (central) store   """
        Stores.bucketlist_store.append(self.bucketlist_stores())
    def update_bucketlist(self, bucketname, bucket_id):
        """ method for updating the bucketlist """
        self.bucketname = bucketname
        self.bucket_id = bucket_id
        return self
    def get_buckets(self):
        """ copies the stored bucketlist and render it to the account """
        view_buckets = Stores.bucketlist_store
        return view_buckets
    def remove_buckets(self, bucket_id):
        """ method used to remove a bucketlist """
        selected_bucket = [x for x in Stores.bucketlist_store[:] if
                           bucket_id == x['bucket_id']]
        Stores.bucketlist_store.remove(selected_bucket['0'])
        return True