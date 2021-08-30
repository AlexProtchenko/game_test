from flask import jsonify, Blueprint, request
from game.repository import GamesRepository
from game.model import Game


game_controller_api = Blueprint('game_controller_api', __name__)


@game_controller_api.route('/api/games', methods=['GET'])
def get_games():
    g = GamesRepository()
    obj = g.get()
    return jsonify(obj)


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
    return 'ok'


@game_controller_api.route('/api/games/<int:id>', methods=['DELETE'])
def delete_game(id):
    g = GamesRepository()
    g.delete(id)
    return 'ok'



