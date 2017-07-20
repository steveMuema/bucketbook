from app.models.store import Stores
""" """
class Activities(object):
    """contains blueprint and methods for accessing activities"""
    def __init__(self, activitytxt, activity_id):
        self.activitytxt = activitytxt
        self.activity_id = activity_id
    def activity_store(self):
        """return information to be called  when appending to the store """
        return{'activitytxt': self.activitytxt,
                'activity_id': self.activity_id,}
    @classmethod
    def create_activity(cls, activitytxt, activity_id):
        """ method for appending created actvities to the activities_store on (central) store   """
        new_activity = cls(activitytxt, activity_id)
        new_activity.save_activity()
    def save_activity(self):
        """ """
        Stores.activities_store.append(self.activity_store())
    def update_activities(self, activitytxt, activity_id):
        """ method for updating the activity """
        self.activitytxt = activitytxt
        self.activity_id = activity_id
        return self
    def get_activities(self):
        """ copies the stored activity and render it to the view """
        view_activities = Stores.activities_store
        return view_activities
    def remove_activity(self, activity_id):
        """method used to remove a activity """
        selected_activity = [x for x in Stores.activities_store if
                             activity_id == x['activity_id']]
        selected_activity.remove()
        return Stores.activities_store
    
    