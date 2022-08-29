from get_tables.table_str3_rus import ts3_rus
from result_mdl.base_rsl import Base_mdl
from strategies.str1.table_1_0 import ts_1_0
from strategies.str1.enex_1_0 import en_1_0
from strategies.str1.enex_1_1 import en_1_1

import statistics as st
import pandas as pd

st_o = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] + 1, 2] - 0) and gf_copy.iloc[ind[i], 2] < 1000 and gf_copy.iloc[ind[i] - 1, 2] < 1000"

class Str1_0_0:

    def __init__(self, market_tick, share_tick, stime='2022-01-01', ftime=None, interval='1wk', str_opt=None):
        self.market_tick = market_tick
        self.share_tick = share_tick
        self.stime = stime
        self.ftime = ftime
        self.interval = interval
        self.srt_opt = str_opt

    def signals(self):
        """   !!!  Add short period  !!!  """
        """ !!! ADD LAST MONTH (NOW JUNE 6) !!! """
        if type(self.share_tick) == str or None:
            x = Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick,
                                       self.stime, self.ftime, self.interval), self.srt_opt)).signal2()
        else:
            copy_names = self.share_tick.copy()
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = (Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick[i],
                                                                 self.stime, self.ftime, self.interval),
                                                          self.srt_opt)).signal2())
                    d = {"Companies": copy_names, 'Signals': self.share_tick}
                except:
                    self.share_tick[i] = 0
            df = pd.DataFrame(data=d)
            x = df[(df.Signals == 'Buy') | (df.Signals == 'Sell') | (df.Signals == 'Buy') | (df.Signals == 'Sell')]
        return x

    def sum_results(self):
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick,
                                                    self.stime, self.ftime, self.interval), self.srt_opt)).rt2()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick[i],
                                                                  self.stime, self.ftime, self.interval), self.srt_opt)).rt2()
                except:
                    self.share_tick[i] = 0
            rs = sum(self.share_tick)
            mean = st.mean(self.share_tick)

            return mean  # rs #self.share_tick, rs

    def sum_results_rus(self):  # неисправлена архитектура
        if len(self.share_tick) == 2:
            self.share_tick = Base_mdl(ts3_rus(*self.share_tick)).rt2()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                x = self.share_tick[i]
                try:
                    self.share_tick[i] = Base_mdl(ts3_rus(*x)).rt2()
                except:
                    self.share_tick[i] = 0
        rs = sum(self.share_tick)
        return self.share_tick, rs

    def get_table(self):
        return en_1_0(ts_1_0(self.market_tick, self.share_tick, self.stime, self.ftime, self.interval), self.srt_opt)


    def month_results(self):
        return Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick,
                                        self.stime, self.ftime, self.interval), self.srt_opt)).date_sum2()

    def month_results_without_bad(self):
        """ WITH LAST CURRENT MONTH (6 now) """
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick,
                                                    self.stime, self.ftime, self.interval), self.srt_opt)).del_any_months()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = list(Base_mdl(en_1_0(ts_1_0(self.market_tick, self.share_tick[i],
                                                                  self.stime, self.ftime, self.interval), self.srt_opt)).del_any_months())
                except:
                    self.share_tick[i] = 0
            rs = sum(self.share_tick)
        return self.share_tick, rs

class Str1_0_1:

    def __init__(self, market_tick, share_tick, stime='2022-01-01', ftime=None, interval='1d', str_opt=None):
        self.market_tick = market_tick
        self.share_tick = share_tick
        self.stime = stime
        self.ftime = ftime
        self.interval = interval
        self.srt_opt = str_opt

    def signals(self):
        """   !!!  Add short period  !!!  """
        """ !!! ADD LAST MONTH (NOW JUNE 6) !!! """
        if type(self.share_tick) == str or None:
            x = Base_mdl(en_1_1(ts_1_0(self.market_tick, self.share_tick,
                                        self.stime, self.ftime, self.interval), self.srt_opt)).signal2()
        else:
            copy_names = self.share_tick.copy()
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = (Base_mdl(en_1_1(ts_1_0(self.market_tick, self.share_tick[i],
                                                                  self.stime, self.ftime, self.interval), self.srt_opt)).signal2())
                    d = {"Companies": copy_names, 'Signals': self.share_tick}
                except:
                    self.share_tick[i] = 0
            df = pd.DataFrame(data=d)
            x = df[(df.Signals == 'Buy') | (df.Signals == 'Sell') | (df.Signals == 'Buy') | (df.Signals == 'Sell')]
        return x

    def sum_results(self):
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(en_1_1(ts_1_0(self.market_tick, self.share_tick,
                                                    self.stime, self.ftime, self.interval), self.srt_opt)).rt2()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = Base_mdl(en_1_1(ts_1_0(self.market_tick, self.share_tick[i],
                                                                  self.stime, self.ftime, self.interval), self.srt_opt)).rt2()
                except:
                    self.share_tick[i] = 0
            rs = sum(self.share_tick)
            mean = st.mean(self.share_tick)

            return mean  # rs #self.share_tick, rs

    def sum_results_rus(self):  # неисправлена архитектура
        if len(self.share_tick) == 2:
            self.share_tick = Base_mdl(ts3_rus(*self.share_tick)).rt2()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                x = self.share_tick[i]
                try:
                    self.share_tick[i] = Base_mdl(ts3_rus(*x)).rt2()
                except:
                    self.share_tick[i] = 0
        rs = sum(self.share_tick)
        return self.share_tick, rs

    def get_table(self):
        return en_1_1(ts_1_0(self.market_tick, self.share_tick, self.stime, self.ftime, self.interval), self.srt_opt)


    def month_results(self):
        return Base_mdl(en_1_1(ts_1_0(self.market_tick, self.share_tick,
                                        self.stime, self.ftime, self.interval), self.srt_opt)).date_sum2()

    def month_results_without_bad(self):
        """ WITH LAST CURRENT MONTH (6 now) """
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(en_1_1(ts_1_0(self.market_tick, self.share_tick,
                                                    self.stime, self.ftime, self.interval), self.srt_opt)).del_any_months()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = list(Base_mdl(en_1_1(ts_1_0(self.market_tick, self.share_tick[i],
                                                                  self.stime, self.ftime, self.interval), self.srt_opt)).del_any_months())
                except:
                    self.share_tick[i] = 0
            rs = sum(self.share_tick)
        return self.share_tick, rs




if __name__ == '__main__':


    print(Str1_0_0('^GSPC', 'Aple',str_opt=a1).get_table())