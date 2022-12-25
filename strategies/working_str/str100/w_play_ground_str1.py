from result_mdl.base_rsl import Base_mdl
from strategies.working_str.str100.w_table_1_0 import ts_1_0
from strategies.working_str.str100.w_enex_1_0 import en_1_0
from strategies.working_str.str100.w_cr_enex_1_0 import cr_en_1_0
import statistics as st
import pandas as pd

btc = 'BTC-USD'
coin_list = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'XRP-USD', 'DOGE-USD', 'ADA-USD', 'MATIC-USD', 'WTRX-USD', 'DOT-USD', 'TRX-USD', 'LTC-USD', 'SHIB-USD', 'SOL-USD', 'HEX-USD', 'STETH-USD', 'UNI7083-USD', 'AVAX-USD', 'LEO-USD', 'LINK-USD', 'TON11419-USD']


class Str1_0_0:

    def __init__(self, market_tick, share_tick, stime='2022-01-01', ftime=None, interval='1wk'):
        self.market_tick = market_tick
        self.share_tick = share_tick
        self.stime = stime
        self.ftime = ftime
        self.interval = interval

    def signals(self):
        if type(self.share_tick) == str or None:
            x = Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick,
                                       self.stime, self.ftime, self.interval))).signal1()
        else:
            copy_names = self.share_tick.copy()
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = (Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick[i],
                                                                 self.stime, self.ftime, self.interval))).signal1())
                    d = {"Companies": copy_names, 'Signals': self.share_tick}
                except:
                    self.share_tick[i] = 0
            df = pd.DataFrame(data=d)
            x = df[(df.Signals == 'Buy') | (df.Signals == 'Sell') | (df.Signals == 'Buy') | (df.Signals == 'Sell')]
        return x

    def signals2(self):
        """   !!!  Add short period  !!!  """
        """ !!! ADD LAST MONTH (NOW JUNE 6) !!! """
        if type(self.share_tick) == str or None:
            x = Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick,
                                       self.stime, self.ftime, self.interval))).signal2()
        else:
            copy_names = self.share_tick.copy()
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = (Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick[i],
                                                                 self.stime, self.ftime, self.interval))).signal2())
                    d = {"Companies": copy_names, 'Signals': self.share_tick}
                except:
                    self.share_tick[i] = 0
            df = pd.DataFrame(data=d)
            x = df[(df.Signals == 'Buy') | (df.Signals == 'Sell') | (df.Signals == 'Buy') | (df.Signals == 'Sell')]
        return x

    def sum_results(self):
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick,
                                                    self.stime, self.ftime, self.interval))).rt2()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick[i],
                                                                  self.stime, self.ftime, self.interval))).rt2()
                except:
                    self.share_tick[i] = 0
            rs = sum(self.share_tick)
            mean = st.mean(self.share_tick)

            return mean  # rs #self.share_tick, rs


    def get_table(self):
        return en_1_0(ts_1_0(self.market_tick, self.share_tick, self.stime, self.ftime, self.interval))


    def month_results(self):
        return Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick,
                                        self.stime, self.ftime, self.interval))).date_sum2()

    def month_results_without_bad(self):
        """ WITH LAST CURRENT MONTH (6 now) """
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick,
                                                    self.stime, self.ftime, self.interval))).del_any_months()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = list(Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick[i],
                                                                  self.stime, self.ftime, self.interval))).del_any_months())
                except:
                    self.share_tick[i] = 0
            rs = sum(self.share_tick)
        return self.share_tick, rs

class Cr_Str1_0_0:

    def __init__(self, market_tick, share_tick, stime='2022-01-01', ftime=None, interval='1wk'):
        self.market_tick = market_tick
        self.share_tick = share_tick
        self.stime = stime
        self.ftime = ftime
        self.interval = interval

    def signals(self):
        if type(self.share_tick) == str or None:
            x = Base_mdl(cr_en_1_0(ts_1_0(self.market_tick, self.share_tick,
                                       self.stime, self.ftime, self.interval))).signal1()
        else:
            copy_names = self.share_tick.copy()
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = (Base_mdl(cr_en_1_0(ts_1_0(self.market_tick, self.share_tick[i],
                                                                 self.stime, self.ftime, self.interval))).signal1())
                    d = {"Companies": copy_names, 'Signals': self.share_tick}
                except:
                    self.share_tick[i] = 0
            df = pd.DataFrame(data=d)
            x = df[(df.Signals == 'Buy') | (df.Signals == 'Sell') | (df.Signals == 'Buy') | (df.Signals == 'Sell')]
        return x

    def signals2(self):
        """   !!!  Add short period  !!!  """
        """ !!! ADD LAST MONTH (NOW JUNE 6) !!! """
        if type(self.share_tick) == str or None:
            x = Base_mdl(cr_en_1_0(ts_1_0(self.market_tick, self.share_tick,
                                       self.stime, self.ftime, self.interval))).signal2()
        else:
            copy_names = self.share_tick.copy()
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = (Base_mdl(cr_en_1_0(ts_1_0(self.market_tick, self.share_tick[i],
                                                                 self.stime, self.ftime, self.interval))).signal2())
                    d = {"Companies": copy_names, 'Signals': self.share_tick}
                except:
                    self.share_tick[i] = 0
            df = pd.DataFrame(data=d)
            x = df[(df.Signals == 'Buy') | (df.Signals == 'Sell') | (df.Signals == 'Buy') | (df.Signals == 'Sell')]
        return x

    def sum_results(self):
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(cr_en_1_0(ts_1_0(self.market_tick, self.share_tick,
                                                    self.stime, self.ftime, self.interval))).rt2()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = Base_mdl(cr_en_1_0(ts_1_0(self.market_tick, self.share_tick[i],
                                                                  self.stime, self.ftime, self.interval))).rt2()
                except:
                    self.share_tick[i] = 0
            rs = sum(self.share_tick)
            mean = st.mean(self.share_tick)

            return mean  # rs #self.share_tick, rs


    def get_table(self):
        return cr_en_1_0(ts_1_0(self.market_tick, self.share_tick, self.stime, self.ftime, self.interval))


    def month_results(self):
        return Base_mdl(cr_en_1_0(ts_1_0(self.market_tick, self.share_tick,
                                        self.stime, self.ftime, self.interval))).date_sum2()

    def month_results_without_bad(self):
        """ WITH LAST CURRENT MONTH (6 now) """
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(cr_en_1_0(ts_1_0(self.market_tick, self.share_tick,
                                                    self.stime, self.ftime, self.interval))).del_any_months()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = list(Base_mdl(cr_en_1_0(ts_1_0(self.market_tick, self.share_tick[i],
                                                                  self.stime, self.ftime, self.interval))).del_any_months())
                except:
                    self.share_tick[i] = 0
            rs = sum(self.share_tick)
        return self.share_tick, rs


if __name__ == '__main__':
    # print(Str1_0_0('^GSPC', ['ACN']).signals())
    print(Cr_Str1_0_0('BTC-USD', coin_list).signals())