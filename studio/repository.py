import pymysql
from config import host, user, password, db_name
# from model import Studio


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


class StudioRepository:
    def __init__(self, connection=connect()):
        self.connection = connection

    def add(self, studio):
        c = self.connection.cursor()
        request = "INSERT INTO studio(name) VALUES (%s);"
        val = studio.name
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def delete(self, studio_id):
        c = self.connection.cursor()
        request = "DELETE FROM studio WHERE id = %s;"
        val = studio_id
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def get(self):
        with self.connection.cursor() as cursor:
            request = "SELECT * FROM studio;"
            cursor.execute(request)
            rows = cursor.fetchall()
            return rows

    # todo add
# g = StudioRepository()
# name = 'testcode'
# studio = Studio(name)
# g.add(studio)


# todo delete
# g = StudioRepository()
# g.delete(6)

#   todo get
# g = StudioRepository()
# print(g.get())