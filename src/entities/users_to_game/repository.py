from src.sql_config import SqlConfig


class UsersToGameRepository:
    def __init__(self, sql_config: SqlConfig):
        self.sql_config = SqlConfig

    def add(self, user_to_game):
        pass

    def delete(self, user_to_game_id):
        pass

    def get(self):
        pass

    def get_games(self, user_to_game_id):
        pass
