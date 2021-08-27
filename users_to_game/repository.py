import pymysql
from config import host, user, password, db_name
# from model import UsersToGame


def connect():
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


class UsersToGameRepository:
    def __init__(self, connection=connect()):
        self.connection = connection

    def add(self, user_to_game):
        c = self.connection.cursor()
        request = "INSERT INTO users_to_game (user_id, game_id) VALUES (%s, %s);"
        val = (user_to_game.user_id, user_to_game.game_id)
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def delete(self, user_to_game_id):
        c = self.connection.cursor()
        request = "DELETE FROM users_to_game WHERE id = %s;"
        val = user_to_game_id
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def get(self):
        with self.connection.cursor() as cursor:
            request = "SELECT * FROM users_to_game;"
            cursor.execute(request)
            rows = cursor.fetchall()
            return rows



    # todo add
# g = UsersToGameRepository()
# user_id = 5
# game_id = 44
# user_to_game = UsersToGame(user_id, game_id)
# g.add(user_to_game)

# todo delete
# g = UsersToGameRepository()
# g.delete(4)

#   todo get
# g = UsersToGameRepository()
# print(g.get())
