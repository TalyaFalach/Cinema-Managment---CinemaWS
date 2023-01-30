from pathlib import Path
import json


class Users_Permissions_DAL:
    def __init__(self):
        self._path = Path(__file__).parent.parent/"files/permissions.json"

    def get_all(self):
        with open(self._path) as f:
            arr = []
            data = json.load(f)
            for d in data["permissions"]:
                arr.append(d)
        return arr

    def get_user_by_id(self, id):
        arr = []
        with open((self._path), 'r')as f:
            users = json.load(f)
            for user in users["permissions"]:
                if str(id) == user["id"]:
                    arr.append(user)
                    return arr[0]

    def create_user(self, obj):
        with open((self._path)) as f:
            data = json.load(f)
            data["permissions"].append(obj)
        with open((self._path), 'w') as f2:

            json.dump(data, f2)

    def update_user(self, id, obj):
        with open((self._path), 'r') as f:
            data = json.load(f)
            for d in data["permissions"]:
                if d["id"] == str(id):
                    d["permissions"] = obj["permissions"]
                    d["id"] = d["id"]

            with open((self._path), 'w') as f2:
                json.dump(data, f2)
            return 'OK'

    def delete_user(self, id):
        with open((self._path), "r") as f:
            data = json.load(f)
            result = list(filter(lambda x: x["id"] != str(id), data["permissions"]))
        with open((self._path), "w") as f2:
            json.dump({"permissions": result}, f2)
        return "Deleted !"
