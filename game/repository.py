from connection import connect
# from model import Game


class GamesRepository:

    def __init__(self, connection=connect()):
        self.connection = connection

    def add(self, game):
        c = self.connection.cursor()
        request = "INSERT INTO games (name, rate, price, studio)" \
                  " VALUES (%s, %s, %s, %s);"
        val = (game.name, game.rate, game.price, game.studio)
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def delete(self, game_id):
        c = self.connection.cursor()
        request = "DELETE FROM games WHERE id = %s;"
        val = game_id
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def edit_rate(self, game_id, game):
        request = "UPDATE games SET rate = %s WHERE id = %s;"
        c = self.connection.cursor()
        val = (game.rate, game_id)
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def edit_price(self, game_id, game):
        request = "UPDATE games SET price = %s WHERE id = %s;"
        c = self.connection.cursor()
        val = (game.price, game_id)
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def get(self):
        with self.connection.cursor() as cursor:
            request = "SELECT * FROM games;"
            cursor.execute(request)
            rows = cursor.fetchall()
            return rows

    # todo add


# g = GamesRepository()
# name = 'bg'
# price = 1
# rate = 1
# studio = 1
# game = Game(name, rate, price, studio)
#
# g.add(game)

# todo delete
# g = GamesRepository()
# g.delete(46)


# todo rate
# g = GamesRepository()
# name = 'a'
# price = 3
# rate = 3
# studio = 1
# game = Game(name, rate, price, studio)
# g.edit_rate(44, game)

# todo rate
# g = GamesRepository()
# name = 'a'
# price = 5
# rate = 3
# studio = 1
# game = Game(name, rate, price, studio)
# g.edit_price(44, game)


#   todo get
# g = GamesRepository()
# print(g.get())
