from flask import jsonify, Blueprint, request
from game.repository import GamesRepository
from game.model import Game
from http import HTTPStatus


game_controller_api = Blueprint('game_controller_api', __name__)


@game_controller_api.route('/api/games', methods=['GET'])
def get_games():
    g = GamesRepository()
    obj = g.get()
    return jsonify(obj), HTTPStatus.OK


@game_controller_api.route('/api/games/post', methods=['POST'])
def post_game():
    request.method = 'POST'
    game_data = request.json
    g = GamesRepository()
    name = game_data["name"]
    price = game_data["price"]
    rate = game_data["rate"]
    studio = game_data["studio"]
    game = Game(name, rate, price, studio)
    g.add(game)
    return '', HTTPStatus.OK


@game_controller_api.route('/api/games/<int:id>', methods=['DELETE'])
def delete_game(id):
    g = GamesRepository()
    g.delete(id)
    return '', HTTPStatus.OK


@game_controller_api.route('/api/games/rate/<int:id>', methods=['PUT'])
def put_rate(id):
    request.method = 'PUT'
    game_data = request.json
    g = GamesRepository()
    name = ''
    price = 0
    rate = game_data["rate"]
    studio = 0
    game = Game(name, rate, price, studio)
    g.edit_rate(id, game)
    return '', HTTPStatus.OK


@game_controller_api.route('/api/games/price/<int:id>', methods=['PUT'])
def put_price(id):
    request.method = 'PUT'
    game_data = request.json
    g = GamesRepository()
    name = ''
    price = game_data["price"]
    rate = 0
    studio = 0
    game = Game(name, rate, price, studio)
    g.edit_price(id, game)
    return '', HTTPStatus.OK
