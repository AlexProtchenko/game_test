
class UsersRepository:
    def __init__(self, connection: str):
        self.connection = connection

    def add(self, user):
        c = self.connection.cursor()
        self.connection.commit()
        c.close()
        self.connection.close()

    def delete(self, user_id):
        c = self.connection.cursor()
        self.connection.commit()
        c.close()
        self.connection.close()

    def get(self):
        with self.connection.cursor() as cursor:
            rows = cursor.fetchall()
            return rows
