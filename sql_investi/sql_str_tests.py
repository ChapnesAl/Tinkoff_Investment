import psycopg2
from sql_investi.sql_configs import host, user, password, dbname, sslmode, port



class Db_str_tests:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            port=port,  # if we use the localhost we don't have to use this parameter
            sslmode=sslmode,  # if we use the localhost we don't have to use this parameter
            database=dbname
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def get_full_table(self):
        with self.connection:
            result = self.cursor.execute("""SElECT * FROM test_100_plus1;""")
            return result, print(self.cursor.fetchall())

    def insert_line_data(self, values):
        with self.connection:
            result = self.cursor.execute(
                f"""INSERT INTO test_100_plus1 (p18_05_20_01, p19_05_20_06, p19_10_21_01,
                                        p20_05_21_10, p21_06_22_04, p22_01, option)
                    VALUES {values}"""
            )
            return result, print("[INFO] Data was successfully inserted")

    def insert_pack_data(self, pack):
        with self.connection:
            y = pack
            for i in y:
                result = self.cursor.execute(
                    f"""INSERT INTO test_100_common_cl_5 (p18_05_20_01, p19_05_20_06, p19_10_21_01,
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

    def create_table(self):
        with self.connection:
            result = self.cursor.execute(
                """CREATE TABLE test_102(
                                    id serial PRIMARY KEY,
                                    p18_05_20_01 numeric NOT NULL,
                                    p19_05_20_06 numeric NOT NULL,
                                    p19_10_21_01 numeric NOT NULL,
                                    p20_05_21_10 numeric NOT NULL,
                                    p21_06_22_04 numeric NOT NULL,
                                    p22_01 numeric NOT NULL,
                                    option varchar(200) NOT NULL);"""
            )
            return result, print("[INFO] Table created successfully")

if __name__ == '__main__':
    Db_str_tests().get_full_table()
