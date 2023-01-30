from DAL.users_file_dal import Users_file_DAL


class Users_From_File_BL:
    def __init__(self):
        self._file_users = Users_file_DAL()
        
    def get_user_by_id(self,id):
        user = self._file_users.get_user_by_id(id)
        return user

    def create_user(self, obj):
        user = self._file_users.create_user(obj)
        return user

    def get_all_users(self):
        users = self._file_users.get_all_users()
        return users

    def update_user(self, id,obj):
        user = self._file_users.update_user(id,obj)
        return user

    def delete_user(self,id):
        result = self._file_users.delete_user(id)
        return result
        
        
