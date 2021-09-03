from flask import Flask

from src.entities.game.controller import GameController
from src.entities.studio.controller import studio_controller_api
from src.entities.users.controller import user_controller_api
from src.entities.users_to_game.controller import utg_controller_api


def create_app() -> Flask:
    app = Flask(__name__)

    game_controller = GameController()

    app.register_blueprint(game_controller.game_controller_api)
    app.register_blueprint(studio_controller_api)
    app.register_blueprint(user_controller_api)
    app.register_blueprint(utg_controller_api)

    return app

