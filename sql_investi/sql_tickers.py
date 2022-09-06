import psycopg2
from sql_investi.sql_configs import host, user, password, db_name


class Db_figi_tick:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def get_full_table(self):
        with self.connection:
            result = self.cursor.execute("""SElECT * FROM tickers;""")
            return result, print(self.cursor.fetchall())


    def get_figi(self, tick):
        with self.connection:
            tick = tick
            self.cursor.execute(f"""SElECT figi FROM tickers WHERE ticker = '{tick}';""")
            x = self.cursor.fetchone()
            return x[0]




if __name__ == '__main__':
    print(Db_figi_tick().get_figi(tick='AAPL'))
    # print(Db_figi_tick().get_full_table())