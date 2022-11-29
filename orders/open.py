from sql_investi.sql_tickers import Db_figi_tick
from tickers import snp_b_15, snp_b_15a, snp_b_15b, snp_b_15c, snp_b_15d, snp_b_15e
from tickers import b_15_plus, b_15_plus_a, b_15_plus_b, b_15_plus_c, b_15_plus_d, b_15_plus_e
from result_mdl.play_ground_str4 import Str4_0_0, Str4_1_1, Str4_2_2
from dif_func.order_book import spread_ob, better_ask
import pandas as pd
from dif_func.yahoo_requests import Yahoo_resp









class Open_1:
    def __init__(self, signal_table):
        self.table = signal_table
        self.token = 't.HeYJv2gR6veA7am91jKdxBc_mqzCB4mvlTMT7KhRWWEHnt56oXqHkhlHuYPoeoxmV2_2mr6I701U18fiIg4RMA'

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
        tbl = self.table.copy(deep=True)
        x = tbl['Companies'].values
        for i in range(len(x)):
            x[i] = spread_ob(self.token, Db_figi_tick().get_figi(x[i]))
        return x

    def add_price(self):
        tbl = self.table.copy(deep=True)
        x = tbl['Companies'].values
        for i in range(len(x)):
            x[i] = better_ask(self.token, Db_figi_tick().get_figi(x[i]))
        return x

    def add_all(self):
        self.table['figi'] = self.add_figi()
        self.table['beta'] = self.add_beta()
        self.table['price'] = self.add_price()
        self.table['spread'] = self.add_spread()
        return self.table

    def before_filter(self):
        pass

    def sum_today_position(self):
        pass

    def open_position(self):
        if self.sum_today_positon < 100:
            tbl = self.add_all()
            x = tbl['Companies'].values
            for i in range(len(x)):
                x[i] = Yahoo_resp(x[i]).beta()

        else:
            print('Your have limit of today position')




if __name__ == '__main__':
    # print(get_beta('^GSPC', ['AAPL','GPS'], '2022-01-01', '2022-08-15', interval='1wk'))
    # print(Str4_2_2('^GSPC', ['AAPL','GPS'], stime='2022-01-01', ftime='2022-08-15', interval='1wk').signals_without_gap())
    # print(Open_1(Str4_2_2('^GSPC', ['AAPL','GPS'], stime='2022-01-01', ftime='2022-08-15', interval='1wk').signals_without_gap()).add_figi())
    # print(Open_1(Str4_2_2('^GSPC', ['AAPL', 'GPS'], stime='2022-01-01', ftime='2022-08-15', interval='1wk').signals_without_gap()).add_beta())
    print(Open_1(Str4_2_2('^GSPC', ['AAPL', 'GPS'], stime='2022-01-01', ftime='2022-08-15', interval='1wk').signals_without_gap()).add_all())
