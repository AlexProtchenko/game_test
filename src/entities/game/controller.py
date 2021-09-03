from flask import jsonify, Blueprint, request
from http import HTTPStatus

from src.entities.game.model import Game
from src.entities.game.repository import GamesRepository


class GameController:
    game_controller_api = Blueprint('game_controller_api', __name__)

    def __init__(self):
        self.game_repository = GamesRepository()

    @game_controller_api.route('/api/games', methods=['GET'])
    def get_games(self):
        obj = self.game_repository.get()
        return jsonify(obj), HTTPStatus.OK

    @game_controller_api.route('/api/games', methods=['GET'])
    def get_games(self):
        obj = self.game_repository.get()
        return jsonify(obj), HTTPStatus.OK

    @game_controller_api.route('/api/games/post', methods=['POST'])
    def post_game(self):
        request.method = 'POST'
        game_data = request.json
        name = game_data["name"]
        price = game_data["price"]
        rate = game_data["rate"]
        studio = game_data["studio"]
        game = Game(name, rate, price, studio)
        self.game_repository.add(game)
        return '', HTTPStatus.OK

    @game_controller_api.route('/api/games/<int:id>', methods=['DELETE'])
    def delete_game(self, _id):
        self.game_repository.delete(_id)
        return '', HTTPStatus.OK

    @game_controller_api.route('/api/games/rate/<int:id>', methods=['PUT'])
    def put_rate(self, _id):
        request.method = 'PUT'
        game_data = request.json
        name = ''
        price = 0
        rate = game_data["rate"]
        studio = 0
        game = Game(name, rate, price, studio)
        self.game_repository.edit_rate(_id, game)
        return '', HTTPStatus.OK

    @game_controller_api.route('/api/games/price/<int:id>', methods=['PUT'])
    def put_price(self, _id):
        request.method = 'PUT'
        game_data = request.json
        name = ''
        price = game_data["price"]
        rate = 0
        studio = 0
        game = Game(name, rate, price, studio)
        self.game_repository.edit_price(_id, game)
        return '', HTTPStatus.OK



