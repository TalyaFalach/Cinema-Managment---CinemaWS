from pathlib import Path
import json


class Users_file_DAL:
    def __init__(self):
        self._path = Path(__file__).parent.parent/"files/users.json"

    def get_all_users(self):
        arr = []
        with open(self._path) as f:
            data = json.load(f)
            for d in data["users"]:
                arr.append(d)
        return arr

    def get_user_by_id(self, id):
        arr = []
        with open((self._path), 'r')as f:
            users = json.load(f)
            for user in users["users"]:
                if str(id) == user["id"]:
                    arr.append(user)
                    return arr[0]

    def create_user(self, obj):
        with open((self._path)) as f:
            data = json.load(f)
            data["users"].append(obj)
        with open((self._path), 'w') as f2:
            json.dump(data, f2)

    def update_user(self, id, obj):
        with open((self._path), 'r') as f:
            data = json.load(f)
            for d in data["users"]:
                if d["id"] == str(id):
                    d["firstName"] = obj["firstName"]
                    d["lastName"] = obj["lastName"]
                    d["sessionTimeOut"] = obj["sessionTimeOut"]

                    d["id"] = d["id"]
            with open((self._path), 'w') as f2:
                json.dump(data, f2)
            return 'OK'

    def delete_user(self, id):
        with open((self._path), "r") as f:
            data = json.load(f)
            result = list(filter(lambda x: x["id"] != str(id),data["users"]))
        with open((self._path), "w") as f2:
            json.dump({"users":result}, f2)
        return "Deleted !"
       
