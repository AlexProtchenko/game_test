from connection import connect


class UsersRepository:
    def __init__(self, connection=connect()):
        self.connection = connection

    def add(self, user):
        c = self.connection.cursor()
        request = "INSERT INTO users (nick) VALUES (%s);"
        val = user.nick
        self.connection.ping()
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def delete(self, user_id):
        c = self.connection.cursor()
        request = "DELETE FROM users WHERE id = %s;"
        val = user_id
        self.connection.ping()
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def get(self):
        with self.connection.cursor() as cursor:
            request = "SELECT * FROM users;"
            self.connection.ping()
            cursor.execute(request)
            rows = cursor.fetchall()
            return rows
