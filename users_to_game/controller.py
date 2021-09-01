from flask import jsonify, Blueprint, request
from users_to_game.repository import UsersToGameRepository
from users_to_game.model import UsersToGame
from http import HTTPStatus


utg_controller_api = Blueprint('utg_controller_api', __name__)


@utg_controller_api.route('/api/utg', methods=['GET'])
def get_utp():
    u = UsersToGameRepository()
    obj = u.get()
    return jsonify(obj), HTTPStatus.OK


@utg_controller_api.route('/api/utg/post', methods=['POST'])
def post_utg():
    request.method = 'POST'
    utg_data = request.json
    u = UsersToGameRepository()
    user_id = utg_data["user_id"]
    game_id = utg_data["game_id"]
    utg = UsersToGame(user_id, game_id)
    u.add(utg)
    return '', HTTPStatus.OK


@utg_controller_api.route('/api/utg/<int:id>', methods=['DELETE'])
def delete_utg(id):
    u = UsersToGameRepository()
    u.delete(id)
    return '', HTTPStatus.OK


@utg_controller_api.route('/api/utg/user/<int:id>', methods=['GET'])
def get_games(id):
    u = UsersToGameRepository()
    obj = u.get_games(id)
    return jsonify(obj), HTTPStatus.OK
