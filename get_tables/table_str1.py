import numpy
import pandas as pd
import yfinance as yf
from pprint import pprint

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

""" Data to add"""
t1 = '^GSPC'
t2 = 'AAPL'


def ts1(market_ticker, stock_ticker):  # table from strategy 1

    # market_ticker = '^GSPC'
    # stock_ticker = 'AAPL'

    # s = 'AAPL'

    """ Get data from efinance API"""

    def get_data_from_ticker(tick):
        ticker = yf.Ticker(tick)
        # df = ticker.history(start='2021-01-01', end='2022-06-02')
        # df = ticker.history(start='2021-01-01')
        df = ticker.history(start='2022-01-01')
        x = pd.DataFrame(df)
        x.rename(columns={"Close": tick}, inplace=True)
        z = x.drop(columns=["Open", "High", "Low", "Volume", "Dividends", "Stock Splits"])
        return z

    gf = pd.DataFrame(get_data_from_ticker(market_ticker))
    sf = pd.DataFrame(get_data_from_ticker(stock_ticker))
    extracted_col = sf[stock_ticker]
    gf[stock_ticker] = extracted_col

    """ Get percent day to day"""

    def add_percent_update(tick):
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
    gf[f'{stock_ticker}-{market_ticker}'] = gf[f"% update {market_ticker}"] - gf[f"% update {stock_ticker}"]

    """ Average desynchronization """
    av_des = gf[f'{stock_ticker}-{market_ticker}']
    av_des = av_des[av_des >= 0]
    r_ac_des = av_des.mean()

    """ Coefficient of divergence"""

    # x = gf.iloc[:, 0]+ gf.iloc[:, 1]
    # x = gf.iloc[:, 3]
    # print(x)

    """ Get coefficients of difference """

    def coef_of_div(dataframe):
        a = dataframe.copy(deep=True)
        m = a.iloc[:, 2]
        s = a.iloc[:, 3]
        # t = s.copy(deep=True)
        t = a.iloc[:, 3]
        for i in range(len(s)):
            if s[i] >= 0 and m[i] >= 0 or s[i] < 0 and m[i] < 0:
                s[i] = s[i] - m[i]
                if s[i] < 0:
                    s[i] = s[i] * -1
                else:
                    pass
                if 1 <= s[i] < 4:
                    t[i] = 2
                elif s[i] > 4:
                    t[i] = 3
                elif 0 <= s[i] < 1:
                    t[i] = 1
                else:
                    pass
            elif s[i] >= 0 > m[i] or s[i] < 0 <= m[i]:
                s[i] = s[i] - m[i]
                if s[i] < 0:
                    s[i] = s[i] * -1
                else:
                    pass
                if s[i] >= 1:
                    t[i] = 3
                elif 0.6 <= s[i] < 1:
                    t[i] = 2
                elif 0 <= s[i] < 0.6:
                    t[i] = 1
                else:
                    pass
            else:
                pass
            # if s[i] < 0 and m[i] < 0:
            #     s[i] = s[i] - m[i]
            #     if s[i] < 0:
            #         s[i] = s[i] * -1
            #     else:
            #         pass
            #     if 1 <= s[i] < 4:
            #         t[i] = 2
            #     elif s[i] > 4:
            #         t[i] = 3
            #     elif 0 <= s[i] < 1:
            #         t[i] = 1
            #     else:
            #         pass
            # else:
            #     pass
            # if s[i] < 0 <= m[i]:
            #     s[i] = s[i] - m[i]
            #     if s[i] < 0:
            #         s[i] = s[i] * -1
            #     else:
            #         pass
            #     if s[i] >= 1:
            #         t[i] = 3
            #     elif 0.6 <= s[i] < 1:
            #         t[i] = 2
            #     elif 0 <= s[i] < 0.6:
            #         t[i] = 1
            #     else:
            #         pass
        return t

    gf['Coef'] = coef_of_div(gf)

    # x = coef_of_div(gf).values
    # for i in x:
    return gf

# tt1(t1,t2)
