import numpy
import pandas as pd
import yfinance as yf

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

""" Data to add"""
t1 = '^GSPC'
t2 = 'acn'


def ts_4_0(market_ticker, stock_ticker):  # table from strategy 1

    # market_ticker = '^GSPC'
    # stock_ticker = 'AAPL'

    # s = 'AAPL'

    def get_data_from_ticker(tick):
        ticker = yf.Ticker(tick)
        # df = ticker.history(start='2021-01-01', end='2022-06-30')
        df = ticker.history(start='2021-01-01', end='2022-07-26')
        # df = ticker.history(start='2020-01-01', end='2021-01-01')
        # df = ticker.history(start='2022-05-28')
        # df = ticker.history(start='2021-01-01')
        x = pd.DataFrame(df)
        x.rename(columns={"Close": tick}, inplace=True)
        z = x.drop(columns=["Open", "High", "Low", "Volume", "Dividends", "Stock Splits"])
        return z

    gf = pd.DataFrame(get_data_from_ticker(market_ticker))
    sf = pd.DataFrame(get_data_from_ticker(stock_ticker))
    extracted_col = sf[stock_ticker]
    gf[stock_ticker] = extracted_col

    def add_percent_update(tick):
        """ date stock's or market's update"""
        gf_copy = gf.copy(deep=True)
        gf_copy = pd.DataFrame(gf_copy.drop(gf.index[0]))
        gf_copy_v = gf_copy[tick].values
        gf_v = gf.copy(deep=True)
        gf_vv = gf_v[tick].values

        for i in range(len(gf_copy)):
            gf_vv[i] = (gf_copy_v[i] - gf_vv[i]) / (gf_vv[i] / 100)

        gf_vv = numpy.insert(gf_vv, 0, 0)
        gf_vv = numpy.delete(gf_vv, -1)
        return gf_vv

    gf[f"% update {market_ticker}"] = add_percent_update(market_ticker)
    gf[f"% update {stock_ticker}"] = add_percent_update(stock_ticker)

    def get_index(table):
        gf_copy = table.copy(deep=True)
        gf_copy = gf_copy.reset_index()
        gf_copy = gf_copy.index.tolist()
        return gf_copy

    index = get_index(gf)

    def add_week_difference_market(table, ind):
        """ Sum of date stock's update"""
        gf_copy = table.copy(deep=True)
        gf_copy2 = table.copy(deep=True)
        t = gf_copy2.iloc[:, 2]
        for i in range(len(ind)):
            try:
                # 7 days
                if gf_copy.iloc[ind[i], 2] in [gf_copy.iloc[0, 2], gf_copy.iloc[1, 2], gf_copy.iloc[2, 2],
                                               gf_copy.iloc[3, 2], gf_copy.iloc[4, 2], gf_copy.iloc[5, 2],
                                               gf_copy.iloc[6, 2]]:
                    t[i] = 0
                else:
                    t[i] = (gf_copy.iloc[ind[i], 2] + gf_copy.iloc[ind[i] - 1, 2] + gf_copy.iloc[ind[i] - 2, 2] +
                            gf_copy.iloc[ind[i] - 3, 2] + gf_copy.iloc[ind[i] - 4, 2] + gf_copy.iloc[ind[i] - 5, 2] +
                            gf_copy.iloc[ind[i] - 6, 2])
            except:
                t[i] = 0
        return t

    gf["Week dif Mar"] = add_week_difference_market(gf, index)

    def add_week_difference_stock(table, ind):
        """ Sum of date stock's update"""
        gf_copy = table.copy(deep=True)
        gf_copy2 = table.copy(deep=True)
        t = gf_copy2.iloc[:, 3]
        for i in range(len(ind)):
            try:
                # 7 days
                if gf_copy.iloc[ind[i], 3] in [gf_copy.iloc[0, 3], gf_copy.iloc[1, 3], gf_copy.iloc[2, 3],
                                               gf_copy.iloc[3, 3], gf_copy.iloc[4, 3], gf_copy.iloc[5, 3],
                                               gf_copy.iloc[6, 3]]:
                    t[i] = 0
                else:
                    t[i] = (gf_copy.iloc[ind[i], 3] + gf_copy.iloc[ind[i] - 1, 3] + gf_copy.iloc[ind[i] - 2, 3] +
                            gf_copy.iloc[ind[i] - 3, 3] + gf_copy.iloc[ind[i] - 4, 3] + gf_copy.iloc[ind[i] - 5, 3] +
                            gf_copy.iloc[ind[i] - 6, 3])
            except:
                t[i] = 0
        return t

    gf["Week dif St"] = add_week_difference_stock(gf, index)

    return gf

if __name__ == '__main__':
    print(ts_4_0(t1, t2))