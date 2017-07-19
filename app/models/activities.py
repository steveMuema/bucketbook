from app.models.store import Stores
class Activities(object):
    def __init__(self, txtActivity):
        self.txtActivity = txtActivity


    """ creates new bucketlist and appends to the store with save_bucketlist"""
    def activity_stores(self):
        """return information to be called  when appending to the store for bucketlist[bucketlist_store]"""
        return{'txtActivity': self.txtActivity}

    @classmethod
    def new_activity(self, txtActivity):
        """ sets the attribute of the class to new_bucketlist and calls save_bucketlist() to append on store"""
        new_activity=self(txtActivity)
        new_activity.save_activity()

    def save_activity(self):
        """ method for appending created txtbucket to the bucketlist_store on (central) store   """
        Stores.activities_store.append(self.activity_stores())
