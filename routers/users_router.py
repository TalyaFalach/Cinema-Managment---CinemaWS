from flask import Blueprint, request, make_response, jsonify
from utils import order_data
from BLL.users_bl import UsersBL
from BLL.users_file_bl import Users_From_File_BL
from BLL.users_permissions_bl import Users_Permissions_File_BL

users_bl = UsersBL()
users_file_bl = Users_From_File_BL()
users_permission_bl = Users_Permissions_File_BL()
users = Blueprint('users', __name__)


@users.route('/', methods=['GET'])
def get_all_users():
    token = None
    # see if token exist
    if request.headers and request.headers.get("x-access-token"):
        token = request.headers.get("x-access-token")
        # if there is token, we need to to Decode to the token, and see if he is exist #! (auth_bl - verify_token())
        exist = users_bl.check_user(token)
        if exist:
            users_db = users_bl.get_users_db()
            users_file = users_file_bl.get_all_users()
            users_permissions = users_permission_bl.get_all_users()

            all_users_data = order_data(
                users_db, users_file, users_permissions)
            return make_response({"users": all_users_data}, 200)
        else:
            return make_response({"error": "no token provided"}, 401)
    else:
        return make_response({"error": "no token provided"}, 401)






@users.route('/<id>', methods=['GET'])
def get_user_by_id(id):
    if request.headers and request.headers.get("x-access-token"):
        token = request.headers.get("x-access-token")
        exist = users_bl.check_user(token)
        if exist:
            user = users_bl.get_user_by_id(id)
            user_file = users_file_bl.get_user_by_id(id)
            user_permission = users_permission_bl.get_user_by_id(id)
            obj = {"username": user["username"], "firstName": user_file["firstName"],
                   "lastName": user_file["lastName"], "createdDate": user_file["createdDate"], "sessionTimeOut": user_file["sessionTimeOut"], "permissions": user_permission["permissions"]}
            if "admin" in user_file.keys():
                obj["admin"] = True
            return make_response({"user": obj}, 200)
           
          
        else:
            return make_response({"error": "error"})


@users.route('/admin', methods=['POST'])
def create_admin_user():
    if request.headers and request.headers.get("x-access-token"):

        username = request.json["username"]
        password = None
        firstName = request.json["firstName"]
        lastName = request.json["lastName"]
        createdDate = request.json["createdDate"]
        sessionTimeOut = request.json["sessionTimeOut"]
        permissions = request.json["permissions"]

        user_id = users_bl.create_admin_user(username, password)
        user_file_obj = {"id": str(user_id), "firstName": firstName, "lastName": lastName,
                         "createdDate": createdDate, "sessionTimeOut": sessionTimeOut}
        user_permissions_obj = {
            "id": str(user_id), "permissions": permissions}

        users_file_bl.create_user(user_file_obj)
        users_permission_bl.create_user(user_permissions_obj)
        return make_response({"user": str(user_id)}, 200)


@users.route('/', methods=['POST'])
def create_user():
    username = request.json["username"]
    password = request.json["password"]
    firstName = request.json["firstName"]
    lastName = request.json["lastName"]
    createdDate = request.json["createdDate"]
    sessionTimeOut = request.json["sessionTimeOut"]
    permissions = request.json["permissions"]
    # add user to the DB and return user_id
    user_id = users_bl.create_user(username, password)

    user_file_obj = {"id": str(user_id), "firstName": firstName, "lastName": lastName,
                     "createdDate": createdDate, "sessionTimeOut": sessionTimeOut}
    user_permissions_obj = {"id": str(user_id), "permissions": permissions}

    users_file_bl.create_user(user_file_obj)
    users_permission_bl.create_user(user_permissions_obj)
    return make_response({"user": str(user_id)}, 200)


@users.route('/<id>', methods=['PUT'])
def update_user(id):

    obj = {"username": request.json["username"],
           "firstName": request.json["firstName"],
           "lastName": request.json["lastName"],
           "sessionTimeOut": request.json["sessionTimeOut"],
           "permissions": request.json["permissions"]}

    user_db = users_bl.update_user(id, obj)
    user_file = users_file_bl.update_user(id, obj)
    user_permissions = users_permission_bl.update_user(id, obj)

    return make_response({"user": user_file})


@users.route('/<id>', methods=['DELETE'])
def delete_user(id):
    users_file_bl.delete_user(id)
    users_permission_bl.delete_user(id)
    user_db = users_bl.delete_user(id)
    return make_response({"success": user_db})
