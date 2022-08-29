import psycopg2
from sql_config import host, user, password, db_name
from sql_ask_collection import get_data, insert_data, create_table, get_full_table, del_row_cond, del_all
from sql_base_asks import ins_tinc_ticr

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

    # insert_data(connection)
    # ins_tinc_ticr(connection)
    # del_all(connection)
    # del_row_cond(connection)
    get_full_table(connection)


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection close")
