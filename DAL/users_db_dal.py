from pymongo import MongoClient
from bson import ObjectId


class Users_db_DAL:
    def __init__(self):
        self._client = MongoClient(port=27017)
        self._db = self._client["cinema"]
        self._collection = self._db["users"]

    def get_all_users(self):
        arr = []
        users = list(self._collection.find({}))
        for user in users:
            arr.append(user)
        return arr

    def get_user_by_id(self, id):
        user = self._collection.find_one({"_id": ObjectId(id)})
        return user

    def create_user(self, obj):
        user_id = (self._collection.insert_one(obj)).inserted_id
        return user_id

    def create_admin_user(self, obj):
        user_id = self._collection.insert_one(obj).inserted_id
        return user_id

    def find_user(self, username, password):
        user = self._collection.find_one(
            {"username": username, "password": password})
        if user:
            return user
        else:
            return None

    def register_new_user(self, username, password, new_password):
        user = self._collection.find_one(
            {"username": username}, {"password": password})

        if user:
            updated_user = self._collection.find_one_and_update(
                {"username": username}, {"$set": {"password": new_password}})
            return updated_user

        else:
            return None

    def update_user(self, id, obj):
        user = self._collection.update_one(
            {"_id": ObjectId(id)}, {"$set": {"_id": ObjectId(id), "username": obj["username"], }})
        return "Updated !"
    
    def delete_user(self,id):
        self._collection.delete_one({"_id":ObjectId(id)})
        return "Deleted !"