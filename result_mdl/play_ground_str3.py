from get_tables.table_str3 import ts3
from get_tables.table_str3_rus import ts3_rus
from result_mdl.base_rsl import Base_mdl
from paper_filter.lists_papers import val_all_usd, val_long_usd, val_long_rub, val_all_rub
import pandas as pd


class Str3:

    def __init__(self, market_tick, share_tick):
        self.market_tick = market_tick
        self.share_tick = share_tick

    '''   !!!  Add short period  !!!  '''
    """ !!! ADD LAST MONTH (NOW JUNE 6) !!! """

    def signals(self):
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


if __name__ == '__main__':
    print(Str3('^GSPC', 'T').signals())
