from flask import jsonify, Blueprint, request
from users.repository import UsersRepository
from users.model import Users
from http import HTTPStatus


user_controller_api = Blueprint('user_controller_api', __name__)


@user_controller_api.route('/api/users', methods=['GET'])
def get_users():
    u = UsersRepository()
    obj = u.get()
    return jsonify(obj), HTTPStatus.OK


@user_controller_api.route('/api/users/post', methods=['POST'])
def post_user():
    request.method = 'POST'
    user_data = request.json
    u = UsersRepository()
    nick = user_data["nick"]
    user = Users(nick)
    u.add(user)
    return '', HTTPStatus.OK


@user_controller_api.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    u = UsersRepository()
    u.delete(id)
    return '', HTTPStatus.OK
