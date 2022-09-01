import psycopg2
# from sql_config import host, user, password, db_name
# from sql_ask_collection import get_data, insert_data, create_table, get_full_table, del_row_cond, del_all
# from sql_base_asks import ins_tinc_ticr


class Db_str_tests:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="127.0.0.1",
            user="postgres",
            password="123234",
            database="trading_bot"
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def get_full_table(self):
        with self.connection:
            result = self.cursor.execute("""SElECT * FROM test_100;""")
            return result, print(self.cursor.fetchall())

    def insert_line_data(self, values):
        with self.connection:
            result = self.cursor.execute(
                f"""INSERT INTO test_100 (p18_05_20_01, p19_05_20_06, p19_10_21_01,
                                        p20_05_21_10, p21_06_22_04, p22_01, option)
                    VALUES {values}"""
            )
            return result, print("[INFO] Data was successfully inserted")

    def insert_pack_data(self, pack):
        with self.connection:
            y = pack
            for i in y:
                result = self.cursor.execute(
                    f"""INSERT INTO test_100 (p18_05_20_01, p19_05_20_06, p19_10_21_01,
                                        p20_05_21_10, p21_06_22_04, p22_01, option)
                    VALUES {i}"""
                )
            return result, print("[INFO] Data was successfully inserted")

    def __del_all(self):
        with self.connection:
            result = self.cursor.execute(
                """DELETE FROM test_100;"""
            )
        return result, print("[INFO] Data was successfully deleted")


if __name__ == '__main__':
    Db_str_tests().insert_datas()
    Db_str_tests().get_full_table()
