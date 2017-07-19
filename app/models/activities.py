from app.models.store import Stores
class Activities(object):
    def __init__(self, activitytxt):
        self.activitytxt = activitytxt
    def activity_stores(self):
        """return information to be called  when appending to the store"""
        return{'activitytxt': self.activitytxt}

    @classmethod
    def new_activity(cls, activitytxt):
        """ sets the attribute of the class to new_activity and append on store"""
        new_activity = cls(activitytxt)
        new_activity.save_activity()

    def save_activity(self):
        """ method for appending created txtbucket to the bucketlist_store on (central) store   """
        Stores.activities_store.append(self.activity_stores())
