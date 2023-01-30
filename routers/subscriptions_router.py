
from flask import Blueprint, request, make_response, jsonify

from BLL.subscriptions_bl import SubscriptionsBL
subscriptions_bl = SubscriptionsBL()

subscriptions = Blueprint('subscriptions', __name__)


@subscriptions.route('/', methods=['GET'])
def get_all():
    subscriptions = subscriptions_bl.get_all()
    return make_response({"data": subscriptions}, 200)


@subscriptions.route('/<id>', methods=['GET'])
def get_by_id(id):
    subscription = subscriptions_bl.get_by_id(id)
    return make_response({"data": subscription}, 200)


@subscriptions.route('/', methods=['POST'])
def create_subscription():
    obj = request.json
    result = subscriptions_bl.create_subscription(obj)
    return make_response({"Success": result}, 200)


@subscriptions.route('/<id>', methods=['POST'])
def add_to_exist_subscription(id):
    
    
    movie = request.json
    result = subscriptions_bl.add_to_exist_subscription(id, movie)
    return make_response({"Success": result}, 200)
