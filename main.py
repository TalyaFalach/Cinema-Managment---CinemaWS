from flask import request, jsonify

import os

from flask import Flask
import json
from flask_cors import CORS
from bson import ObjectId
from routers.auth_router import auth
from routers.users_router import users
from routers.movies_router import movies
from routers.members_router import members
from routers.subscriptions_router import subscriptions



class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


app = Flask(__name__)

app.url_map.strict_slashes = False
CORS(app)
app.json_encoder = JSONEncoder
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(users, url_prefix="/users")
app.register_blueprint(movies, url_prefix="/movies")
app.register_blueprint(members, url_prefix="/members")
app.register_blueprint(subscriptions, url_prefix="/subscriptions")


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run()
    
    


