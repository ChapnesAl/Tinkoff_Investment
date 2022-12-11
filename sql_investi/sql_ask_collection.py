


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
            """SElECT * FROM test_100;"""
        )
        tupples = cursor.fetchall()
        return tupples


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
            """CREATE TABLE test_100(
                id serial PRIMARY KEY,
                p18_05_20_01 decimal(30) NOT NULL,
                p19_05_20_06 decimal(30) NOT NULL,
                p19_10_21_01 decimal(30) NOT NULL,
                p20_05_21_10 decimal(30) NOT NULL,
                p21_06_22_04 decimal(30) NOT NULL,
                p22_01 decimal(30) NOT NULL,
                option varchar(200) NOT NULL);"""
        )
        print("[INFO] Table created successfully")


if __name__ == '__main__':
    print(get_data())