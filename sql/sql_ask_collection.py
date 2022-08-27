
connection = None


# def get_data():
#     r = """SElECT figi FROM tickers WHERE ticker = 'GGG';"""
#     return r

def insert_data(connect):
    with connect.cursor() as cursor:
        cursor.execute(
            """INSERT INTO tickers (ticker, figi)
            VALUES ('BBB', 'rasd');"""
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

def create_table(connect):
    with connect.cursor() as cursor:
        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE tickers(
                id serial PRIMARY KEY,
                ticker varchar(20) NOT NULL,
                figi varchar(20) NOT NULL);"""
            )
            print("[INFO] Table created successfully")


# print(get_data())