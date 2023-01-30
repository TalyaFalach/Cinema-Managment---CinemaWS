import jwt
# from BLL.users_bl import UsersBL
from DAL.users_db_dal import Users_db_DAL
from DAL.users_file_dal import Users_file_DAL

from datetime import datetime, timedelta
from datetime import timezone


class AuthBL:
    def __init__(self):
        self._key = "server_key"
        self._algorithm = "HS256"

    def get_token(self, username, password):
        users_file_dal = Users_file_DAL()
        # if user exist, create the token from user id
        token = None
        user = self._check_user(username, password)
        user_id = str(user["_id"])
        if user_id == "63b40e43d7c406ea3e4914e3":
            token = jwt.encode({"user_id": user_id},
                               self._key, self._algorithm)
            return {"token": token, "user": user}
        else:

            user_session_time_out = users_file_dal.get_user_by_id(user_id)["sessionTimeOut"]
            
            payload = {"user_id": user_id, "exp": datetime.utcnow(
            )+timedelta(minutes=int(user_session_time_out))}

            token = jwt.encode(payload, self._key, self._algorithm)
            return {"token": token, "user": user}

    def _check_user(self, username, password):
        users_db = Users_db_DAL()
        encoded_password = jwt.encode(
            {"password": password}, self._key, self._algorithm)
        user = users_db.find_user(username, encoded_password)
        if user is not None:
            return user
        else:
            return None

    def verify_token(self, token):
        data = jwt.decode(token, self._key, self._algorithm)
        user_id = data["user_id"]
        if user_id:
            return True
        else:
            return False
        # check existance of that user in db, if exist - return true. else - false

    def encode_password(self, password):
        # function that encode the password to add to the database
        encoded_password = jwt.encode(
            {"password": password}, self._key, self._algorithm)
        return encoded_password
