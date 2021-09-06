from sqlalchemy import MetaData, Table, Column, Integer, VARCHAR


def describe_table(metadata: MetaData):
    return Table(
        "studio",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("name", VARCHAR(100), nullable=False)
    )


class StudioRepository:
    def __init__(self, connection: str):
        self.connection = connection

    def add(self, studio):
        c = self.connection.cursor()
        val = studio.name
        self.connection.ping()
        self.connection.commit()
        c.close()
        self.connection.close()

    def delete(self, studio_id):
        c = self.connection.cursor()
        val = studio_id
        self.connection.ping()
        self.connection.commit()
        c.close()
        self.connection.close()

    def get(self):
        with self.connection.cursor() as cursor:
            rows = cursor.fetchall()
            return rows
