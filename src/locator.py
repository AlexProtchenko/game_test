from src.entities.game.repository import GamesRepository
from src.sql_config import SqlConfig


class AppConfig:
    games_repository: GamesRepository = 0

    @staticmethod
    def initialize(sql_config: SqlConfig):
        AppConfig.games_repository = GamesRepository(sql_config)
        # AppConfig.studio_repository = StuRep(sql_config)...
