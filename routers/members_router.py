from flask import Blueprint, request, make_response, jsonify

from BLL.members_bl import MembersBL

members_bl = MembersBL()

members = Blueprint('members', __name__)


@members.route('/', methods=['GET'])
def get_all_members():
    members = members_bl.get_all_members()
    return make_response({"members": members})


@members.route('/<id>', methods=['GET'])
def get_member(id):
    member = members_bl.get_member(id)
    return make_response({"Member": member}, 200)


@members.route('/', methods=['POST'])
def create_member():
    obj = {"name": request.json["name"],
           "email": request.json["email"], "city": request.json["city"]}
    result = members_bl.create_member(obj)
    return make_response({"userId": result}, 200)


@members.route('/<id>', methods=['PUT'])
def update_member(id):
    obj = {"name": request.json["name"],
           "email": request.json["email"], "city": request.json["city"]}
    result = members_bl.update_member(id, obj)
    return make_response({"Update": result}, 200)


@members.route('/<id>', methods=['DELETE'])
def delete_member(id):
    result = members_bl.delete_member(id)
    return make_response({"deleted": result}, 200)
