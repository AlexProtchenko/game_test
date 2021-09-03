import pymysql
from src.config import host, user, password, db_name


def load():
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with connection.cursor() as cursor:
                create_table_query = "CREATE TABLE `studio`(id int AUTO_INCREMENT PRIMARY KEY," \
                                     " name varchar(100) NOT NULL);"
                cursor.execute(create_table_query)

            with connection.cursor() as cursor:
                create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT PRIMARY KEY," \
                                     " nick varchar(100) NOT NULL);"
                cursor.execute(create_table_query)

            with connection.cursor() as cursor:
                create_table_query = "CREATE TABLE `games`(id int AUTO_INCREMENT PRIMARY KEY, " \
                                     "name varchar(100) NOT NULL, " \
                                     "rate float NOT NULL, " \
                                     "price float NOT NULL, " \
                                     "studio int NOT NULL, " \
                                     "FOREIGN KEY (studio) references studio(id));"

                cursor.execute(create_table_query)
            with connection.cursor() as cursor:
                create_table_query = "CREATE TABLE `users_to_game`(id int AUTO_INCREMENT PRIMARY KEY, " \
                                     "user_id int NOT NULL," \
                                     "FOREIGN KEY (user_id) references users(id)," \
                                     "game_id int NOT NULL," \
                                     "FOREIGN KEY (game_id) references games(id));"
                cursor.execute(create_table_query)

        finally:
            connection.close()
    except Exception as ex:
        print(ex)


load()
