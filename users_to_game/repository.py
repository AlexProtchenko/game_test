from connection import connect


class UsersToGameRepository:
    def __init__(self, connection=connect()):
        self.connection = connection

    def add(self, user_to_game):
        c = self.connection.cursor()
        request = "INSERT INTO users_to_game (user_id, game_id) VALUES (%s, %s);"
        val = (user_to_game.user_id, user_to_game.game_id)
        self.connection.ping()
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def delete(self, user_to_game_id):
        c = self.connection.cursor()
        request = "DELETE FROM users_to_game WHERE id = %s;"
        val = user_to_game_id
        self.connection.ping()
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def get(self):
        with self.connection.cursor() as cursor:
            request = "SELECT * FROM users_to_game;"
            self.connection.ping()
            cursor.execute(request)
            rows = cursor.fetchall()
            return rows

    def get_games(self, user_to_game_id):
        with self.connection.cursor() as cursor:
            request = "SELECT * FROM users_to_game WHERE user_id = %s;"
            val = user_to_game_id
            self.connection.ping()
            cursor.execute(request, val)
            rows = cursor.fetchall()
            return rows
