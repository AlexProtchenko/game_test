from connection import connect


class GamesRepository:

    def __init__(self, connection=connect()):
        self.connection = connection

    def add(self, game):
        c = self.connection.cursor()
        request = "INSERT INTO games (name, rate, price, studio)" \
                  " VALUES (%s, %s, %s, %s);"
        val = (game.name, game.rate, game.price, game.studio)
        self.connection.ping()
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def delete(self, game_id):
        c = self.connection.cursor()
        request = "DELETE FROM games WHERE id = %s;"
        val = game_id
        self.connection.ping()
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def edit_rate(self, game_id, game):
        request = "UPDATE games SET rate = %s WHERE id = %s;"
        c = self.connection.cursor()
        val = (game.rate, game_id)
        self.connection.ping()
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def edit_price(self, game_id, game):
        request = "UPDATE games SET price = %s WHERE id = %s;"
        c = self.connection.cursor()
        val = (game.price, game_id)
        self.connection.ping()
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def get(self):
        with self.connection.cursor() as cursor:
            request = "SELECT * FROM games;"
            self.connection.ping()
            cursor.execute(request)
            rows = cursor.fetchall()
            return rows
