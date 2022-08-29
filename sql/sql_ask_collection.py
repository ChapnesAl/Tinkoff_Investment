




def insert_data(connect):
    with connect.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO tickers (ticker, figi)
            VALUES {(('GOG', 'rude'), ('GOG', 'rade'))} ;"""
        )
        print("[INFO] Data was successfully inserted")


def get_data(connect):
    with connect.cursor() as cursor:
        cursor.execute(
            """SElECT figi FROM tickers WHERE ticker = 'GGG';"""
        )
        print(cursor.fetchone())

def get_full_table(connect):
    with connect.cursor() as cursor:
        cursor.execute(
            """SElECT * FROM tickers;"""
        )
        print(cursor.fetchall())

def del_row_cond(connect):
    with connect.cursor() as cursor:
        cursor.execute(
            """DELETE FROM tickers WHERE ticker = 'GGG';"""
        )
        print("[INFO] Data was successfully deleted")

def del_all(connect):
    with connect.cursor() as cursor:
        cursor.execute(
            """DELETE FROM tickers;"""
        )
        print("[INFO] Data was successfully deleted")

def create_table(connect):
    with connect.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE tickers(
                id serial PRIMARY KEY,
                ticker varchar(20) NOT NULL,
                figi varchar(20) NOT NULL);"""
        )
        print("[INFO] Table created successfully")


if __name__ == '__main__':

    print(get_data())