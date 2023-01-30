from DAL.users_db_dal import Users_db_DAL
from DAL.users_file_dal import Users_file_DAL
from DAL.users_permissions_file_dal import Users_Permissions_DAL
from BLL.auth_bl import AuthBL


class UsersBL:
    def __init__(self):
        self._users_db = Users_db_DAL()
        self._users_file = Users_file_DAL()
        self._users_permissions = Users_Permissions_DAL()
    
    def get_user_by_id(self,id):
        user = self._users_db.get_user_by_id(id)
        return user

    def get_users_db(self):
        users = self._users_db.get_all_users()
        return users

    def create_admin_user(self, username, password):
        obj = {"username": username, "password": password}
        user = self._users_db.create_admin_user(obj)
        return user

    def check_user(self, token):
        auth_bl = AuthBL()
        exist = auth_bl.verify_token(token)
        return exist

    def create_user(self, username, password):
        auth_bl = AuthBL()
        encoded_password = auth_bl.encode_password(password)
        obj = {"username": username, "password": encoded_password}
        user = self._users_db.create_user(obj)
        return user
    
    
    
    
    def register_new_user(self, username, password, new_password):
        auth_bl = AuthBL()
        encoded_password = auth_bl.encode_password(new_password)
        user = self._users_db.register_new_user(
            username, password, encoded_password)
        return user
    
    def update_user(self,id,obj):
        user = self._users_db.update_user(id,obj)
        return user
    
    def delete_user(self,id):
        result = self._users_db.delete_user(id)
        return result
