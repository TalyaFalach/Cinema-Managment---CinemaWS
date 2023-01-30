from DAL.subscriptions_dal import SubscriptionsDal
class SubscriptionsBL:
    def __init__(self):
        self._subscriptions = SubscriptionsDal()

    def get_all(self):
        data = self._subscriptions.get_all()
        return data
    
    def get_by_id(self, id):
        res =self._subscriptions.get_by_id(id)
        return res
   
   #! POST
    def create_subscription(self, obj):
        data = self._subscriptions.create_subscription(obj)
        return data
    
    def add_to_exist_subscription(self, id, movie):
        result = self._subscriptions.add_to_exist_subscription(id,movie)
        return result
