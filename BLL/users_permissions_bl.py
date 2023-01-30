from DAL.users_permissions_file_dal import Users_Permissions_DAL


class Users_Permissions_File_BL:
    def __init__(self):
        self._file_permissions = Users_Permissions_DAL()

    def get_all_users(self):
        users = self._file_permissions.get_all()
        return users


    def get_user_by_id(self, id):
        user = self._file_permissions.get_user_by_id(id)
        return user

    def create_user(self, obj):
        user = self._file_permissions.create_user(obj)
        return user
    
    def update_user(self, id, obj):
        user = self._file_permissions.update_user(id, obj)
        return user
    
    def delete_user(self,id):
        result = self._file_permissions.delete_user(id)
        return result
