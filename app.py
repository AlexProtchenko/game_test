from flask import Flask
from game.controller import game_controller_api
from studio.controller import studio_controller_api
from users.controller import user_controller_api
from users_to_game.controller import utg_controller_api


def create_app():
    app = Flask(__name__)

    app.register_blueprint(game_controller_api)
    app.register_blueprint(studio_controller_api)
    app.register_blueprint(user_controller_api)
    app.register_blueprint(utg_controller_api)

    if __name__ == "__main__":
        return app


c = create_app()
c.run()
