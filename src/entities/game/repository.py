from sqlalchemy import MetaData, Table, Column, Integer, VARCHAR, Float, ForeignKey

from src.entities.game.model import Game
from src.sql_config import SqlConfig


GAMES: Table


def describe_table(metadata: MetaData) -> Table:
    return Table(
        "games",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("name", VARCHAR(100), nullable=False),
        Column("rate", Float, nullable=False),
        Column("price", Float, nullable=False),
        Column("studio", Float, nullable=False)  # Foreign Key Studio ID
    )


class GamesRepository:  # todo create rep and init into app.py
    def __init__(self, sql_config: SqlConfig):
        global GAMES
        GAMES = describe_table(sql_config.metadata)

        self.engine = sql_config.engine

    def add(self, game: Game):
        statement = GAMES.insert().values(
            name=game.name,
            rate=game.rate,
            price=game.price,
            studio=game.studio
        )
        with self.engine.begin() as connection:
            connection.execute(statement)

    def delete(self, game_id):
        statement = GAMES.delete().where(
            GAMES.c.id == game_id
        )
        with self.engine.begin() as connection:
            connection.execute(statement)

    def get(self):
        statement = GAMES.select()

        with self.engine.begin() as connection:
            rows = connection.execute(statement).all()

        return [row.name for row in rows]

    def _row_to_game(self, row) -> Game:
        return Game(
            name=row.name,
            # continue ...
        )

# todo add return
# todo self._rows_to_game():
