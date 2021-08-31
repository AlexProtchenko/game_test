from connection import connect
# from model import Studio


class StudioRepository:
    def __init__(self, connection=connect()):
        self.connection = connection

    def add(self, studio):
        c = self.connection.cursor()
        request = "INSERT INTO studio(name) VALUES (%s);"
        val = studio.name
        self.connection.ping()
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def delete(self, studio_id):
        c = self.connection.cursor()
        request = "DELETE FROM studio WHERE id = %s;"
        val = studio_id
        self.connection.ping()
        c.execute(request, val)
        self.connection.commit()
        c.close()
        self.connection.close()

    def get(self):
        with self.connection.cursor() as cursor:
            request = "SELECT * FROM studio;"
            self.connection.ping()
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