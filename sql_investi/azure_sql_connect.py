import psycopg2

host="stockschapnes.postgres.database.azure.com"
port=5432
dbname='postgres'
user="chapnes"
password="House333!"
sslmode="require"



connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=dbname,
            sslmode=sslmode)

connection.autocommit = True
cursor = connection.cursor()

def get_full_table():
    with connection:
        result = cursor.execute("""SElECT * FROM test_101;""")
        return result, print(cursor.fetchall())



def create_table():
    with connection:
        result = cursor.execute(
            """CREATE TABLE test_day_100_common_cl_4(
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
    create_table()