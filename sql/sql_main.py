import psycopg2
from sql_config import host, user, password, db_name
from sql_ask_collection import get_data


connection = None

try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")



        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """CREATE TABLE tickers(
        #         id serial PRIMARY KEY,
        #         ticker varchar(20) NOT NULL,
        #         figi varchar(20) NOT NULL);"""
        #     )
        #     print("[INFO] Table created successfully")

        # with connection.cursor() as cursor:
        #     cursor.execute(
        #         """INSERT INTO tickers (ticker, figi)
        #         VALUES ('GGG', 'ghgh');"""
        #     )
        #     print("[INFO] Data was successfully inserted")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SElECT figi FROM tickers WHERE ticker = 'GGG';"""
    #     )
    #     print(cursor.fetchone())

    get_data(connection)


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection close")
