from flask import Flask

from src.locator import AppConfig
from src.sql_config import SqlConfig
from src.entities.game.controller import game_controller_api
from src.entities.studio.controller import studio_controller_api
from src.entities.users.controller import user_controller_api
from src.entities.users_to_game.controller import utg_controller_api


def create_app(connection: str) -> Flask:
    app = Flask(__name__)

    sql_config = SqlConfig(connection)  # todo load reps with sql_config

    AppConfig.initialize(sql_config)

    app.register_blueprint(game_controller_api)
    app.register_blueprint(studio_controller_api)
    app.register_blueprint(user_controller_api)
    app.register_blueprint(utg_controller_api)

    sql_config.metadata.create_all(checkfirst=True)

    return app




