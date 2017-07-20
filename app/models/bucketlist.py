""" This module contains fundamentals of the bucketlists class"""
from app.models.store import Stores
from app.models.activities import Activities
"""Attributes: buckets 'used to instantiate a bucketlist and also save value to store', 
               buckets_index 'returns the index of particular index'  """                
class Bucketlist(object):
    """ class will contain fundamentals for bucketlists"""
    def __init__(self, buckets):
        """ initiate list of  buckets and add empty list of activities to a new bucket"""
        self.buckets = buckets
        self.activities = Activities.new_activity("")
        # self.buckets_index = buckets.index('buckets')
    def buckets_stores(self):
        """return information to be called  when appending to the store """
        return{'buckets': self.buckets}
    @classmethod
    def create_buckets(cls, buckets, activities, bucket_index):
        """ creates a bucketlist with its attributes"""
        #pylint: disable-msg=E1121
        new_bucket = cls(buckets, activities, 
                         len(buckets.index(Stores.bucket)).append(bucket_index))
        Stores.bucket.append(new_bucket)
    @classmethod
    def create_bucketlist(cls, buckets):
        new_bucketlist = cls(buckets)
        new_bucketlist.save_bucketlist()
    def save_bucketlist(self):
        """ method for appending created buckets to the buckets_store on (central) store   """
        Stores.bucketlist_store.append(self.buckets_stores())

    def get_buckets(self):
        """ copies the stored bucketlist and render it to the account """
        view_buckets = Stores.bucketlist_store
        return view_buckets
    
    def view_buckets_activities(self, activities):
        """ View activities of a specific bucketlist by
        1. copies the bucketlist_store
        1.search index of current bucketlist
        1. copies the items in the current bucketlist
        2. return the activities in the current bucketlist"""
        #copy the bucketlist_store
        current_bucketlist_store = Stores.bucketlist_store
        try: 
            bucket_index = current_bucketlist_store.index(activities)
            return bucket_index
        except ValueError:
            return None

    @classmethod
    def remove_buckets(self,buckets):
        bucket_list=self(buckets)
        all_indexes = len(Stores.bucketlist_store)
        for bucket_index in range(all_indexes):
            if bucket_index == Stores.bucketlist_store.pop(bucket_index):
                Stores.bucketlist_store.remove(bucket_index)
        # except ValueError:
        #     return None
        return bucket_list
