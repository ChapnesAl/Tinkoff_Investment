from get_tables.table_str3_rus import ts3_rus
from result_mdl.base_rsl import Base_mdl
from strategies.str3.table_3_0 import ts3_0
from strategies.str3.table_3_1 import ts3_1
from strategies.str3.enex_3_0 import en_3_0_0
from strategies.str3.enex_3_1 import en_3_0_1
import pandas as pd


class Str3_0_0:

    def __init__(self, market_tick, share_tick):
        self.market_tick = '^GSPC'
        self.share_tick = share_tick

    def signals(self):
        """   !!!  Add short period  !!!  """
        """ !!! ADD LAST MONTH (NOW JUNE 6) !!! """
        if type(self.share_tick) == str or None:
            x = Base_mdl(en_3_0_0(ts3_0(self.market_tick, self.share_tick))).signal2()
        else:
            copy_names = self.share_tick.copy()
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = (Base_mdl(en_3_0_0(ts3_0(self.market_tick, self.share_tick[i]))).signal2())
                    d = {"Companies": copy_names, 'Signals': self.share_tick}
                except:
                    self.share_tick[i] = 0
            df = pd.DataFrame(data=d)
            x = df[(df.Signals == 'Buy') | (df.Signals == 'Sell') | (df.Signals == 'Buy') | (df.Signals == 'Sell')]
        return x

    def sum_results(self):
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(en_3_0_0(ts3_0(self.market_tick, self.share_tick))).rt2()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = Base_mdl(en_3_0_0(ts3_0(self.market_tick, self.share_tick[i]))).rt2()
                except:
                    self.share_tick[i] = 0
            rs = sum(self.share_tick)
        return self.share_tick, rs

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
        return en_3_0_0(ts3_0(self.market_tick,self.share_tick))


    def month_results(self):
        return Base_mdl(en_3_0_0(ts3_0(self.market_tick, self.share_tick))).date_sum2()

    def month_results_without_bad(self):
        """ WITH LAST CURRENT MONTH (6 now) """
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(en_3_0_0(ts3_0(self.market_tick, self.share_tick))).del_any_months()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = list(Base_mdl(en_3_0_0(ts3_0(self.market_tick, self.share_tick[i]))).del_any_months())
                except:
                    self.share_tick[i] = 0
            rs = sum(self.share_tick)
        return self.share_tick, rs

class Str3_0_1:

    def __init__(self, market_tick, share_tick):
        self.market_tick = '^GSPC'
        self.share_tick = share_tick

    def signals(self):
        """   !!!  Add short period  !!!  """
        """ !!! ADD LAST MONTH (NOW JUNE 6) !!! """
        if type(self.share_tick) == str or None:
            x = Base_mdl(en_3_0_1(ts3_0(self.market_tick, self.share_tick))).signal2()
        else:
            copy_names = self.share_tick.copy()
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = (Base_mdl(en_3_0_1(ts3_0(self.market_tick, self.share_tick[i]))).signal2())
                    d = {"Companies": copy_names, 'Signals': self.share_tick}
                except:
                    self.share_tick[i] = 0
            df = pd.DataFrame(data=d)
            x = df[(df.Signals == 'Buy') | (df.Signals == 'Sell') | (df.Signals == 'Buy') | (df.Signals == 'Sell')]
        return x

    def sum_results(self):
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(en_3_0_1(ts3_0(self.market_tick, self.share_tick))).rt2()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = Base_mdl(en_3_0_1(ts3_0(self.market_tick, self.share_tick[i]))).rt2()
                except:
                    self.share_tick[i] = 0
            rs = sum(self.share_tick)
        return self.share_tick, rs

    def sum_results_rus(self): # неисправлена архитектура
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
        return en_3_0_1(ts3_0(self.market_tick,self.share_tick))


    def month_results(self):
        return Base_mdl(en_3_0_1(ts3_0(self.market_tick, self.share_tick))).date_sum2()

    def month_results_without_bad(self):
        """ WITH LAST CURRENT MONTH (6 now) """
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(en_3_0_1(ts3_0(self.market_tick, self.share_tick))).del_any_months()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = list(Base_mdl(en_3_0_1(ts3_0(self.market_tick, self.share_tick[i]))).del_any_months())
                except:
                    self.share_tick[i] = 0
            rs = sum(self.share_tick)
        return self.share_tick, rs

class Str3_1_1:

    def __init__(self, market_tick, share_tick, stime='2022-01-01', ftime=None, interval='1d'):
        self.market_tick = market_tick
        self.share_tick = share_tick
        self.stime = stime
        self.ftime = ftime
        self.interval = interval

    def signals(self):
        """   !!!  Add short period  !!!  """
        """ !!! ADD LAST MONTH (NOW JUNE 6) !!! """
        if type(self.share_tick) == str or None:
            x = Base_mdl(en_3_0_1(ts3_1(self.market_tick, self.share_tick,
                                        self.stime, self.ftime, self.interval))).signal2()
        else:
            copy_names = self.share_tick.copy()
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = (Base_mdl(en_3_0_1(ts3_1(self.market_tick, self.share_tick[i],
                                                                  self.stime, self.ftime, self.interval))).signal2())
                    d = {"Companies": copy_names, 'Signals': self.share_tick}
                except:
                    self.share_tick[i] = 0
            df = pd.DataFrame(data=d)
            x = df[(df.Signals == 'Buy') | (df.Signals == 'Sell') | (df.Signals == 'Buy') | (df.Signals == 'Sell')]
        return x

    def sum_results(self):
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(en_3_0_1(ts3_1(self.market_tick, self.share_tick,
                                                                  self.stime, self.ftime, self.interval))).rt2()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = Base_mdl(en_3_0_1(ts3_1(self.market_tick, self.share_tick[i],
                                                                  self.stime, self.ftime, self.interval))).rt2()
                except:
                    self.share_tick[i] = 0
            rs = sum(self.share_tick)
        return self.share_tick, rs

    def sum_results_rus(self): # неисправлена архитектура
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
        return en_3_0_1(ts3_1(self.market_tick, self.share_tick,
                                    self.stime, self.ftime, self.interval))


    def month_results(self):
        return Base_mdl(en_3_0_1(ts3_1(self.market_tick, self.share_tick,
                                         self.stime, self.ftime, self.interval))).date_sum2()

    def month_results_without_bad(self):
        """ WITH LAST CURRENT MONTH (6 now) """
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(en_3_0_1(ts3_1(self.market_tick, self.share_tick,
                                                     self.stime, self.ftime, self.interval))).del_any_months()
            rs = ''
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = list(Base_mdl(en_3_0_1(ts3_1(self.market_tick, self.share_tick[i],
                                                                  self.stime, self.ftime, self.interval))).del_any_months())
                except:
                    self.share_tick[i] = 0
            rs = sum(self.share_tick)
        return self.share_tick, rs

if __name__ == '__main__':
    # print(Str3('^GSPC', 'T').signals())
    # print(Str3( 'T').sum_results())
    # print(Str3('^GSPC', 'T').get_table())
    print(Str3_0_0('^GSPC', 'T').month_results())
    # print(Str3('^GSPC', ['T', 'AA']).month_results_without_bad())
    # print(Str3('^GSPC', val_all_rub).sum_results_rus())
