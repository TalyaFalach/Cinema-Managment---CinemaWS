from DAL.Members_dal import MembersDAL

class MembersBL:
    def __init__(self):
        self._members = MembersDAL()
        
#! GET all
    def get_all_members(self):
        members = self._members.get_all_members()
        return members

#! GET
    def get_member(self, id):
        member = self._members.get_member(id)
        return member

#! POST
    def create_member(self, obj):
        data = self._members.create_member(obj)
        return data

#! PUT
    def update_member(self, id, obj):
        data = self._members.update_member(id,obj)
        return data

#! DELETE
    def delete_member(self, id):
        data = self._members.delete_member(id)
        return data
