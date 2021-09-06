from flask import jsonify, Blueprint, request, current_app as app
from http import HTTPStatus

from src.entities.game.model import Game

game_controller_api = Blueprint('game_controller_api', __name__)


@game_controller_api.route('/api/games', methods=['GET'])
def get_games():
    obj = app.config.game_repository.get()
    return jsonify(obj), HTTPStatus.OK

#
# @game_controller_api.route('/api/games/post', methods=['POST'])
# def post_game():
#     request.method = 'POST'
#     game_data = request.json
#     name = game_data["name"]
#     price = game_data["price"]  # todo request.load() -> Game
#     rate = game_data["rate"]
#     studio = game_data["studio"]
#     game = Game(name, rate, price, studio)
#     qc = game_repository
#     game_repository.add(game)
#     return '', HTTPStatus.OK
#
#
# @game_controller_api.route('/api/games/<int:_id>', methods=['DELETE'])
# def delete_game(_id):
#     game_repository.delete(_id)
#     return '', HTTPStatus.OK
#
#
# @game_controller_api.route('/api/games/rate/<int:_id>', methods=['PUT'])
# def put_rate(_id):
#     request.method = 'PUT'
#     game_data = request.json
#     name = ''
#     price = 0
#     rate = game_data["rate"]
#     studio = 0
#     game = Game(name, rate, price, studio)
#     game_repository.edit_rate(_id, game)
#     return '', HTTPStatus.OK
#
#
# @game_controller_api.route('/api/games/price/<int:_id>', methods=['PUT'])
# def put_price(_id):
#     request.method = 'PUT'
#     game_data = request.json
#     name = ''
#     price = game_data["price"]
#     rate = 0
#     studio = 0
#     game = Game(name, rate, price, studio)
#     game_repository.edit_price(_id, game)
#     return '', HTTPStatus.OK
