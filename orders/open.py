from sql_investi.sql_tickers import Db_figi_tick


from tickers import snp_b_15, snp_b_15a, snp_b_15b, snp_b_15c, snp_b_15d, snp_b_15e
from tickers import b_15_plus, b_15_plus_a, b_15_plus_b, b_15_plus_c, b_15_plus_d, b_15_plus_e
from result_mdl.play_ground_str4 import Str4_0_0, Str4_1_1, Str4_2_2
import pandas as pd
from dif_func.yahoo_requests import Yahoo_resp

def get_beta(market, stock, s_time, f_time=None, interval='1d'):
    df = Str4_2_2(market, stock, stime=s_time, ftime=f_time, interval=interval).signals_without_gap()
    df_copy = df.copy(deep=True)
    tickers = df_copy['Companies'].values
    for i in range(len(tickers)):
        tickers[i] = Yahoo_resp(tickers[i]).beta()
    df['beta'] = tickers

    return df

df = get_beta('^GSPC', ['AAPL','GPS'], '2022-01-01', '2022-08-15', interval='1wk')


import psycopg2
from sql_investi.sql_configs import host, user, password, db_name









class Open_1:
    def __init__(self, signal_table):
        self.table = signal_table

    def add_figi(self):
        tbl = self.table.copy(deep=True)
        x = tbl['Companies'].values
        for i in range(len(x)):
            x[i] = Db_figi_tick().get_figi(x[i])
        return x

    def add_beta(self):
        tbl = self.table.copy(deep=True)
        x = tbl['Companies'].values
        for i in range(len(x)):
            x[i] = Yahoo_resp(x[i]).beta()
        return x

    def add_spread(self):
        pass


    def add_price(self):
        pass



    def add_all(self):
        pass

    def open_position(self):
        pass







if __name__ == '__main__':
    # print(get_beta('^GSPC', ['AAPL','GPS'], '2022-01-01', '2022-08-15', interval='1wk'))
    # print(Str4_2_2('^GSPC', ['AAPL','GPS'], stime='2022-01-01', ftime='2022-08-15', interval='1wk').signals_without_gap())
    print(Open_1(Str4_2_2('^GSPC', ['AAPL','GPS'], stime='2022-01-01', ftime='2022-08-15', interval='1wk').signals_without_gap()).add_figi())