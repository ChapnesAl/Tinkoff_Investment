from sql_investi.sql_main import main_sql_ask
import pandas as pd
import psycopg2
import sys





# column_names = ['p18_05_20_01', 'p19_05_20_06', 'p19_10_21_01', 'p20_05_21_10', 'p22_01', 'option']


# df = pd.read_sql_table(main_sql_ask(), con=)

# Connection parameters, yours will be different
param_dic = {
    "host"      : "127.0.0.1",
    "database"  : "trading_bot",
    "user"      : "postgres",
    "password"  : "123234"
}
def connect(params_dic):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params_dic)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit(1)
    print("Connection successful")
    return conn




def postgresql_to_dataframe(conn, select_query, column_names):
    """
    Tranform a SELECT query into a pandas dataframe
    """
    cursor = conn.cursor()
    try:
        cursor.execute(select_query)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        cursor.close()
        return 1

    # Naturally we get a list of tupples
    tupples = cursor.fetchall()
    cursor.close()

    # We just need to turn it into a pandas dataframe
    df = pd.DataFrame(tupples, columns=column_names)
    return df



# Connect to the database
conn = connect(param_dic)
# column_names = ["id", "source", "datetime", "mean_temp"]
column_names = ["id", "p18_05_20_01", "p19_05_20_06", "p19_10_21_01", "p20_05_21_10", "p21_06_22_01", "p22_01", "option"]

# Execute the "SELECT *" query
# df = postgresql_to_dataframe(conn, "select * from test_100", column_names)
# df.head()


# MY SOLUTION
df = pd.DataFrame(main_sql_ask(), columns=column_names)


if __name__ == '__main__':
    print(df.head())
