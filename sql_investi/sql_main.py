import psycopg2
from sql_investi.sql_configs import host, user, password, db_name
from sql_investi.sql_ask_collection import get_data, insert_data, create_table, get_full_table, del_row_cond, del_all
from sql_investi.sql_base_asks import ins_tinc_tic





def main_sql_ask():
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

        result = insert_data(connection)
        # result = ins_tinc_tic(connection)
        # result = del_all(connection)
        # result = del_row_cond(connection)
        # result = create_table(connection)
        result = get_full_table(connection)
        # result = get_data(connection)


    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL connection close")
    return result

if __name__ == '__main__':
    main_sql_ask()