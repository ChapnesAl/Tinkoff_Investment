import numpy
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
from pprint import pprint

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

""" Data to add"""
t1 = '^GSPC'
t2 = 'GT'


def ts2(market_ticker, stock_ticker):  # table from strategy 1

    # market_ticker = '^GSPC'
    # stock_ticker = 'AAPL'

    # s = 'AAPL'

    def get_data_from_ticker(tick):
        ticker = yf.Ticker(tick)
        df = ticker.history(start='2019-01-01', end='2021-01-01')
        # df = ticker.history(start='2021-01-01')
        # df = ticker.history(start='2022-07-11')
        x = pd.DataFrame(df)
        x.rename(columns={"Close": tick}, inplace=True)
        z = x.drop(columns=["Open", "High", "Low", "Volume", "Dividends", "Stock Splits"])
        return z

    gf = pd.DataFrame(get_data_from_ticker(market_ticker))
    sf = pd.DataFrame(get_data_from_ticker(stock_ticker))
    extracted_col = sf[stock_ticker]
    gf[stock_ticker] = extracted_col

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
    # gf[f'{stock_ticker}-{market_ticker}'] = gf[f"% update {market_ticker}"] - gf[f"% update {stock_ticker}"]


    def get_index(table):
        gf_copy = table.copy(deep=True)
        gf_copy = gf_copy.reset_index()
        gf_copy = gf_copy.index.tolist()
        return gf_copy

    index = get_index(gf)


    def add_week_difference(table, ind):
        gf_copy = table.copy(deep=True)
        gf_copy2 = table.copy(deep=True)
        t = gf_copy2.iloc[:, 3]
        for i in range(len(ind)):
            try:
                # 3 days
                t[i] = (gf_copy.iloc[ind[i], 3] + gf_copy.iloc[ind[i]-1, 3] + gf_copy.iloc[ind[i]-2, 3]) - (gf_copy.iloc[ind[i], 2]
                        + gf_copy.iloc[ind[i]-1, 2] + gf_copy.iloc[ind[i]-2, 2])
                # 7 days
                # t[i] = (gf_copy.iloc[ind[i], 3] + gf_copy.iloc[ind[i]-1, 3] + gf_copy.iloc[ind[i]-2, 3] + gf_copy.iloc[ind[i]-3, 3]
                #         + gf_copy.iloc[ind[i]-4, 3] + gf_copy.iloc[ind[i]-5, 3] + gf_copy.iloc[ind[i]-6, 3]) - (gf_copy.iloc[ind[i], 2]
                #         + gf_copy.iloc[ind[i]-1, 2] + gf_copy.iloc[ind[i]-2, 2] + gf_copy.iloc[ind[i]-3, 2]
                #         + gf_copy.iloc[ind[i]-4, 2] + gf_copy.iloc[ind[i]-5, 2] + gf_copy.iloc[ind[i]-6, 2])
                # 16 days
                # t[i] = (gf_copy.iloc[ind[i], 3] + gf_copy.iloc[ind[i]-1, 3] + gf_copy.iloc[ind[i]-2, 3] + gf_copy.iloc[ind[i]-3, 3]
                #         + gf_copy.iloc[ind[i]-4, 3] + gf_copy.iloc[ind[i]-5, 3] + gf_copy.iloc[ind[i]-6, 3] + gf_copy.iloc[ind[i]-7, 3] + gf_copy.iloc[ind[i]-8, 3] + gf_copy.iloc[ind[i]-9, 3]+ gf_copy.iloc[ind[i]-10, 3] + gf_copy.iloc[ind[i]-11, 3] + gf_copy.iloc[ind[i]-12, 3]+ gf_copy.iloc[ind[i]-13, 3] + gf_copy.iloc[ind[i]-14, 3] + gf_copy.iloc[ind[i]-15, 3]) \
                #        - (gf_copy.iloc[ind[i], 2] + gf_copy.iloc[ind[i]-1, 2] + gf_copy.iloc[ind[i]-2, 2] + gf_copy.iloc[ind[i]-3, 2]
                #         + gf_copy.iloc[ind[i]-4, 2] + gf_copy.iloc[ind[i]-5, 2] + gf_copy.iloc[ind[i]-6, 2]+ gf_copy.iloc[ind[i]-7, 2] + gf_copy.iloc[ind[i]-8, 2] + gf_copy.iloc[ind[i]-9, 2] + gf_copy.iloc[ind[i]-10, 2] + gf_copy.iloc[ind[i]-11, 2] + gf_copy.iloc[ind[i]-12, 2] + gf_copy.iloc[ind[i]-13, 2] + gf_copy.iloc[ind[i]-14, 2] + gf_copy.iloc[ind[i]-15, 2])
            except:
                t[i] = 0
        return t

    gf["Week differ"] = add_week_difference(gf, index)
    # print(gf)

    def signal_to_deal(table, ind):
        gf_copy = table.copy(deep=True)
        r = gf_copy.iloc[:, 3]
        for i in range(len(ind)):
            try:
                if gf_copy.iloc[ind[i], 4] > 0 and gf_copy.iloc[ind[i]-1, 4] < 0:
                    r[i] = 1 # buy
                elif gf_copy.iloc[ind[i], 4] < 0 and gf_copy.iloc[ind[i]-1, 4] > 0:
                    r[i] = 2 # sell
                else:
                    r[i] = 0
            except:
                r[i] = 0
        return r

    gf["Signal"] = signal_to_deal(gf, index)
    # print(gf)

    def result_of_strategy(table, ind):
        gf_copy = table.copy(deep=True)
        t = gf_copy.iloc[:, 3]
        for i in range(len(ind)):
            try:
                if gf_copy.iloc[ind[i], 5] == 1:
                    t[i] = gf_copy.iloc[ind[i]+1, 3]  # buy
                elif gf_copy.iloc[ind[i], 5] == 2:
                    t[i] = gf_copy.iloc[ind[i]+1, 3] * -1  # sell
                else:
                    t[i] = 0
            except:
                t[i] = 0

        return t

    gf["Results"] = result_of_strategy(gf, index)
    # print(gf)
    # print(gf['Results'].sum())

    """All table and sum of result"""
    # return gf['Results'].sum()
    # return gf

    # def send_signal(table):
    #     gf_copy = table.copy(deep=True)
    #     if gf_copy.iloc[-1, 5] == 1.0:
    #         a = 'Buy'
    #     elif gf_copy.iloc[-1, 5] == 2.0:
    #         a ='Sell'
    #     else:
    #        return

        # return a

    return gf


def ts2_minutes(stock_ticker):  # table from strategy 1

    # market_ticker = '^GSPC'
    # stock_ticker = 'AAPL'

    # s = 'AAPL'

    def get_data_from_ticker(tick):
        ticker = yf.Ticker(tick)
        df = ticker.history(interval='15m', period='1d')
        # df = ticker.history(start='2022-01-01')
        x = pd.DataFrame(df)
        x.rename(columns={"Close": tick}, inplace=True)
        z = x.drop(columns=["Open", "High", "Low", "Volume", "Dividends", "Stock Splits"])
        return z

    gf = pd.DataFrame(get_data_from_ticker(stock_ticker))


    return gf #gf.nsmallest(1, stock_ticker), gf.nlargest(1, stock_ticker)




if __name__ == "__main__":
   print(ts2(t1,t2))
   # print(ts2_minutes(t2))
