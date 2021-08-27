from connection import connect
# from model import Users


class UsersRepository:
    def __init__(self, connection=connect()):
        self.connection = connection

    def add(self, user):
        c = self.connection.cursor()
        request = "INSERT INTO users (nick) VALUES (%s);"
        val = user.nick
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def delete(self, user_id):
        c = self.connection.cursor()
        request = "DELETE FROM users WHERE id = %s;"
        val = user_id
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def get(self):
        with self.connection.cursor() as cursor:
            request = "SELECT * FROM users;"
            cursor.execute(request)
            rows = cursor.fetchall()
            return rows


    # todo add
# g = UsersRepository()
# nick = 'aaa'
# user = Users(nick)
# g.add(user)

# todo delete
# g = UsersRepository()
# g.delete(6)

  # todo get
# g = UsersRepository()
# print(g.get())