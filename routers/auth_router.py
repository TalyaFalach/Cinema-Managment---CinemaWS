from flask import Blueprint, request, make_response, session, app
from datetime import timedelta
from BLL.auth_bl import AuthBL
from BLL.users_bl import UsersBL
from flask import Flask, session
from datetime import timedelta
from flask_login import login_user, logout_user
from BLL.users_file_bl import Users_file_DAL

auth_bl = AuthBL()
auth = Blueprint('auth', __name__)
secret_key = "abc"


@auth.route('/login', methods=['POST'])
def login():

    username = request.json["username"]
    password = int(request.json["password"])

    data = auth_bl.get_token(username, password)
    user = data["user"]
    user_id = user["_id"]


    if data["token"] is not None:
        if str(user_id) == "63b40e43d7c406ea3e4914e3":
            return make_response({"user_id": user_id, "token": data["token"]}, 200)
     
        else:
            users_file = Users_file_DAL()
            user_from_file = users_file.get_user_by_id(user_id)

            session.permanent = True
            app.permanent_session_lifetime = timedelta(
                minutes=int(user_from_file["sessionTimeOut"]))
            is_login = auth_bl.verify_token(data["token"])
            if is_login:
                return make_response({"token": data["token"], "user_id": user_id}, 200)

    else:
        return make_response({"error": "Your'e Not Authorized"}, 401)


@auth.route('/register', methods=['POST'])
def register():
    # check if username exist
    # check if password = null
    # create a new password
    users_bl = UsersBL()
    username = request.json["username"]
    password = None
    new_password = int(request.json["password"])
    user = users_bl.register_new_user(username, password, new_password)
    if user is not None:
        return make_response({"user": user}, 200)
    else:
        return make_response({"error": "User Not Exist"}, 401)
