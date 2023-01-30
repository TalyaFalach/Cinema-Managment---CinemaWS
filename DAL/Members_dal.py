import requests

class MembersDAL:
    def __init__(self):
        self._members = "http://localhost:5001/members"
 
#! GET all        
    def get_all_members(self):
        res = requests.get(self._members)
        return res.json()
#! GET
    def get_member(self, id):
        res = requests.get(self._members + "/" + str(id))
        return res.json()

#! POST
    def create_member(self,obj):
        res = requests.post(self._members, json=obj)
        return res.json()
    
#! PUT
    def update_member(self,id,obj):
        res = requests.put(self._members+'/'+str(id), json=obj)
        return res.json()
#! DELETE
    def delete_member(self,id):
        res = requests.delete(self._members+'/'+str(id))
        return res.json()
    
    
    