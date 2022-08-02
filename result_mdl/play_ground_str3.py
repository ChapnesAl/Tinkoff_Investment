from get_tables.table_str3 import ts3
from get_tables.table_str3_rus import ts3_rus
from result_mdl.base_rsl import Base_mdl
from paper_filter.lists_papers import val_all_usd, val_long_usd, val_long_rub, val_all_rub
import pandas as pd


class Str3:

    def __init__(self, market_tick, share_tick):
        self.market_tick = market_tick
        self.share_tick = share_tick

    def signals(self):
        """   !!!  Add short period  !!!  """
        """ !!! ADD LAST MONTH (NOW JUNE 6) !!! """
        if type(self.share_tick) == str or None:
            x = Base_mdl(ts3(self.market_tick, self.share_tick)).signal2()
        else:
            copy_names = self.share_tick.copy()
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = (Base_mdl(ts3(self.market_tick, self.share_tick[i])).signal2())
                    d = {"Companies": copy_names, 'Signals': self.share_tick}
                except:
                    self.share_tick[i] = 0
            df = pd.DataFrame(data=d)
            x = df[(df.Signals == 'Buy') | (df.Signals == 'Sell') | (df.Signals == 'Buy') | (df.Signals == 'Sell')]
        return x

    def sum_results(self):
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(ts3(self.market_tick, self.share_tick)).rt2()
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = Base_mdl(ts3(self.market_tick, self.share_tick[i])).rt2()
                except:
                    self.share_tick[i] = 0
        return self.share_tick

    def get_table(self):
        return ts3(self.market_tick, self.share_tick)

    def month_results(self):
        return Base_mdl(ts3(self.market_tick, self.share_tick)).date_sum2()

    def month_results_without_bad(self):
        """ WITH LAST CURRENT MONTH (6 now) """
        if type(self.share_tick) == str:
            self.share_tick = Base_mdl(ts3(self.market_tick, self.share_tick)).del_any_months()
        else:
            for i in range(len(self.share_tick)):
                try:
                    self.share_tick[i] = list(Base_mdl(ts3(self.market_tick, self.share_tick[i])).del_any_months())
                except:
                    self.share_tick[i] = 0
        return self.share_tick


if __name__ == '__main__':
    # print(Str3('^GSPC', 'T').signals())
    # print(Str3('^GSPC', ['T', 'AA']).sum_results())
    # print(Str3('^GSPC', 'T').get_table())
    # print(Str3('^GSPC', 'T').month_results())
    print(Str3('^GSPC', ['T', 'AA', 'ssdsds']).month_results_without_bad())
