import requests


class SubscriptionsDal:
    def __init__(self):
        self._subscriptions = "http://localhost:5001/subscriptions"

    def get_all(self):
        res = requests.get(self._subscriptions)
        data = res.json()
        return data
    
    def get_by_id(self,id):
        res = requests.get(self._subscriptions +"/" + str(id))
        return res.json()
    
    def create_subscription(self,obj):
        res = requests.post(self._subscriptions, json=obj)
        return res.json()
    
    def add_to_exist_subscription(self,id,movie):
        res = requests.post(self._subscriptions +"/" + str(id), json=movie)
        return res.json()
    
    
        
    
