




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

# a = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2018-05-01', ftime='2020-01-01', interval='1wk', str_opt=st_o).sum_results()
#     b = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2019-05-01', ftime='2020-06-01', interval='1wk', str_opt=st_o).sum_results()
#     c = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2019-10-01', ftime='2021-01-01', interval='1wk', str_opt=st_o).sum_results()
#     d = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2020-05-01', ftime='2021-10-01', interval='1wk', str_opt=st_o).sum_results()
#     e = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2021-06-01', ftime='2022-04-03', interval='1wk', str_opt=st_o).sum_results()
#
#     f = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2022-01-01', interval='1wk', str_opt=st_o).sum_results()
if __name__ == '__main__':

    print(get_data())