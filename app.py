from flask import Flask
from game.controller import game_controller_api
app = Flask(__name__)

app.register_blueprint(game_controller_api)

if __name__ == "__main__":
    app.run()