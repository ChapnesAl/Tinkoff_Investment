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
t2 = 'acn'


def ts3(market_ticker, stock_ticker):  # table from strategy 1

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

    # gf[f'{stock_ticker}-{market_ticker}'] = gf[f"% update {market_ticker}"] - gf[f"% update {stock_ticker}"]

    def get_index(table):
        gf_copy = table.copy(deep=True)
        gf_copy = gf_copy.reset_index()
        gf_copy = gf_copy.index.tolist()
        return gf_copy

    index = get_index(gf)

    def add_week_difference(table, ind):
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

    gf["Week differ Stock"] = add_week_difference(gf, index)

    # print(gf)

    def signal_to_deal(table, ind, tick):
        """ Long and Short"""
        gf_copy = table.copy(deep=True)
        gf_copy = gf_copy.astype({tick: str}, errors='ignore')
        r = gf_copy[tick].values

        for i in range(len(ind)):
            try:

                if gf_copy.iloc[ind[i], 4] > 0 and gf_copy.iloc[ind[i], 4] < 2 \
                        and gf_copy.iloc[ind[i] - 1, 4] > 2.5 and gf_copy.iloc[ind[i] - 1, 4] < 10 \
                        and gf_copy.iloc[ind[i] - 2, 4] > 5 and gf_copy.iloc[ind[i] - 2, 4] < 15 \
                        and gf_copy.iloc[ind[i] - 3, 4] > 0 and gf_copy.iloc[ind[i] - 3, 4] < 25 \
                        and gf_copy.iloc[ind[i] - 4, 4] > 0 and gf_copy.iloc[ind[i] - 4, 4] < 20 \
                        and gf_copy.iloc[ind[i] - 5, 4] < 20 \
                        and gf_copy.iloc[ind[i], 3] < 4:




                    r[i] = 'Short'  # buy
                    # r[i] = 1  # buy
                elif gf_copy.iloc[ind[i], 4] < 0 and gf_copy.iloc[ind[i], 4] > -2 \
                        and gf_copy.iloc[ind[i] - 1, 4] < -2.5 and gf_copy.iloc[ind[i] - 1, 4] > -30 \
                        and gf_copy.iloc[ind[i] - 2, 4] < 5 and gf_copy.iloc[ind[i] - 2, 4] > -40 \
                        and gf_copy.iloc[ind[i] - 3, 4] < -1 and gf_copy.iloc[ind[i] - 3, 4] > -30 \
                        and gf_copy.iloc[ind[i] - 4, 4] < 10 \
                        and gf_copy.iloc[ind[i], 3] > -10\
                        and gf_copy.iloc[ind[i]-1, 3] > -10:

                    # and gf_copy.iloc[ind[i] - 5, 4] < 20:
                    r[i] = 'Long'  # sell
                    # r[i] = 2
                else:
                    r[i] = '0'
                    # r[i] = 0
            except:
                r[i] = '0'
                # r[i] = 0
        return r


    # def signal_to_deal(table, ind, tick):
    #     """ Long only"""
    #     gf_copy = table.copy(deep=True)
    #     gf_copy = gf_copy.astype({tick: str}, errors='ignore')
    #     r = gf_copy[tick].values
    #
    #     for i in range(len(ind)):
    #         try:
    #
    #             if gf_copy.iloc[ind[i], 4] < 0 and gf_copy.iloc[ind[i], 4] > -2 \
    #                     and gf_copy.iloc[ind[i] - 1, 4] < -2.5 and gf_copy.iloc[ind[i] - 1, 4] > -30 \
    #                     and gf_copy.iloc[ind[i] - 2, 4] < 5 and gf_copy.iloc[ind[i] - 2, 4] > -40 \
    #                     and gf_copy.iloc[ind[i] - 3, 4] < -1 and gf_copy.iloc[ind[i] - 3, 4] > -30 \
    #                     and gf_copy.iloc[ind[i] - 4, 4] < 10:
    #                 # and gf_copy.iloc[ind[i] - 5, 4] < 20:
    #                 r[i] = 'Long'  # sell
    #                 # r[i] = 2
    #             else:
    #                 r[i] = '0'
    #                 # r[i] = 0
    #         except:
    #             r[i] = '0'
    #             # r[i] = 0
    #     return r

    """ Сигнал когда недельная разница переходит из минуса в плюс и наоборот"""
    # def signal_to_deal(table, ind, tick):
    #     gf_copy = table.copy(deep=True)
    #     gf_copy = gf_copy.astype({tick:str},errors='ignore')
    #     r = gf_copy[tick].values
    #     a = 1
    #     b = 1
    #     for i in range(len(ind)):
    #         try:
    #
    #             if gf_copy.iloc[ind[i], 4] > 0 and gf_copy.iloc[ind[i]-1, 4] < 0:
    #                 r[i] = f'Long {a}' # buy
    #                 a += 1
    #                 # r[i] = 1  # buy
    #             elif gf_copy.iloc[ind[i], 4] < 0 and gf_copy.iloc[ind[i]-1, 4] > 0:
    #                 r[i] = f'Short {b}' # sell
    #                 b += 1
    #                 # r[i] = 2
    #             else:
    #                 r[i] = '0'
    #                 # r[i] = 0
    #         except:
    #             r[i] = '0'
    #             # r[i] = 0
    #     return r

    gf["Signal"] = signal_to_deal(gf, index, stock_ticker)

    # print(gf)

    def result_of_strategy(table, ind, tick):
        gf_copy = table.copy(deep=True)
        t = gf_copy[tick].values
        for i in range(len(ind)):
            try:
                if gf_copy.iloc[ind[i], 5] == 'Long':
                    t[i] = gf_copy.iloc[ind[i] + 1, 3]  # buy
                elif gf_copy.iloc[ind[i], 5] == 'Short':
                    t[i] = gf_copy.iloc[ind[i] + 1, 3] * -1  # sell
                else:
                    t[i] = 0
            except:
                t[i] = 0

        return t

    #
    gf["Results"] = result_of_strategy(gf, index, stock_ticker)

    # print(gf)

    #     """All table and sum of result"""
    #     # return gf['Results'].sum()
    #     # return gf
    #
    #     # def send_signal(table):
    #     #     gf_copy = table.copy(deep=True)
    #     #     if gf_copy.iloc[-1, 5] == 1.0:
    #     #         a = 'Buy'
    #     #     elif gf_copy.iloc[-1, 5] == 2.0:
    #     #         a ='Sell'
    #     #     else:
    #     #        return
    #
    #         # return a
    #
    #     # return gf
    #
    def stock_vs_market(table, ind, tick):
        gf_copy = table.copy(deep=True)
        gf_copy2 = table.copy(deep=True)
        t = gf_copy2[tick].values
        for i in range(len(ind)):
            try:
                # 3 days
                t[i] = (gf_copy.iloc[ind[i], 3] + gf_copy.iloc[ind[i] - 1, 3] + gf_copy.iloc[ind[i] - 2, 3]) - (
                        gf_copy.iloc[ind[i], 2]
                        + gf_copy.iloc[ind[i] - 1, 2] + gf_copy.iloc[ind[i] - 2, 2])
            except:
                t[i] = 0
        return t

    gf["Stock/market"] = stock_vs_market(gf, index, stock_ticker)

    return gf  # gf.nsmallest(1, stock_ticker), gf.nlargest(1, stock_ticker)


def ts4(market_ticker, stock_ticker):  # table from strategy 1

    # market_ticker = '^GSPC'
    # stock_ticker = 'AAPL'

    # s = 'AAPL'

    def get_data_from_ticker(tick):
        ticker = yf.Ticker(tick)
        # df = ticker.history(start='2021-01-01', end='2022-06-30')
        # df = ticker.history(start='2021-01-01', end='2022-07-26')
        df = ticker.history(start='2020-01-01', end='2021-01-01')
        # df = ticker.history(start='2022-04-20')
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

    gf["Week differ"] = add_week_difference(gf, index)

    # print(gf)

    def signal_to_deal(table, ind, tick):
        gf_copy = table.copy(deep=True)
        gf_copy = gf_copy.astype({tick: str}, errors='ignore')
        r = gf_copy[tick].values

        for i in range(len(ind)):
            try:

                if gf_copy.iloc[ind[i], 4] > 0 and gf_copy.iloc[ind[i], 4] < 2 and gf_copy.iloc[ind[i] - 1, 4] > 2.5:
                    r[i] = 'Short'  # buy
                    # r[i] = 1  # buy
                elif gf_copy.iloc[ind[i], 4] < 0 and gf_copy.iloc[ind[i], 4] > -2 and gf_copy.iloc[
                    ind[i] - 1, 4] < -2.5:
                    r[i] = 'Long'  # sell
                    # r[i] = 2
                else:
                    r[i] = '0'
                    # r[i] = 0
            except:
                r[i] = '0'
                # r[i] = 0
        return r

    """ Сигнал когда недельная разница переходит из минуса в плюс и наоборот"""

    # def signal_to_deal(table, ind, tick):
    #     gf_copy = table.copy(deep=True)
    #     gf_copy = gf_copy.astype({tick:str},errors='ignore')
    #     r = gf_copy[tick].values
    #     a = 1
    #     b = 1
    #     for i in range(len(ind)):
    #         try:
    #
    #             if gf_copy.iloc[ind[i], 4] > 0 and gf_copy.iloc[ind[i]-1, 4] < 0:
    #                 r[i] = f'Long {a}' # buy
    #                 a += 1
    #                 # r[i] = 1  # buy
    #             elif gf_copy.iloc[ind[i], 4] < 0 and gf_copy.iloc[ind[i]-1, 4] > 0:
    #                 r[i] = f'Short {b}' # sell
    #                 b += 1
    #                 # r[i] = 2
    #             else:
    #                 r[i] = '0'
    #                 # r[i] = 0
    #         except:
    #             r[i] = '0'
    #             # r[i] = 0
    #     return r

    # gf["Signal"] = signal_to_deal(gf, index, stock_ticker)

    # print(gf)

    # def marker_dif(table, ind, tick):
    #     gf_copy = table.copy(deep=True)
    #     gf_copy2 = table.copy(deep=True)
    #     t = gf_copy2[tick].values
    #     for i in range(len(ind)):
    #         try:
    #             if ind[i] == 0:
    #                 t[i] = 0
    #             elif ind[i] == 1:
    #                 t[i] = 0
    #             elif ind[i] == 2:
    #                 t[i] = 0
    #             elif ind[i] == 3:
    #                 t[i] = 0
    #             else:
    #                 # 3 days
    #                 t[i] = 100 - (gf_copy.iloc[ind[i] - 3, 0] / (gf_copy.iloc[ind[i], 0] / 100))
    #         except:
    #             t[i] = 0
    #     return t
    #
    # gf["Market-3"] = marker_dif(gf, index, stock_ticker)

    def stock_dif(table, ind, tick):
        gf_copy = table.copy(deep=True)
        gf_copy2 = table.copy(deep=True)
        t = gf_copy2[tick].values
        for i in range(len(ind)):
            try:
                if ind[i] == 0:
                    t[i] = 0
                elif ind[i] == 1:
                    t[i] = 0
                elif ind[i] == 2:
                    t[i] = 0
                elif ind[i] == 3:
                    t[i] = 0
                elif ind[i] == 4:
                    t[i] = 0
                elif ind[i] == 5:
                    t[i] = 0
                else:
                    # 3 days
                    t[i] = 100 - (gf_copy.iloc[ind[i] - 5, 1] / (gf_copy.iloc[ind[i], 1] / 100))
            except:
                t[i] = 0
        return t

    gf["Stock-5"] = stock_dif(gf, index, stock_ticker)

    def stock_dif_sum(table, ind, tick):
        gf_copy = table.copy(deep=True)
        gf_copy2 = table.copy(deep=True)
        t = gf_copy2[tick].values
        for i in range(len(ind)):
            try:
                if ind[i] == 0:
                    t[i] = 0
                elif ind[i] == 1:
                    t[i] = 0
                elif ind[i] == 2:
                    t[i] = 0
                elif ind[i] == 3:
                    t[i] = 0
                elif ind[i] == 4:
                    t[i] = 0
                elif ind[i] == 5:
                    t[i] = 0
                elif ind[i] == 6:
                    t[i] = 0
                else:
                    # 7 days
                    t[i] = gf_copy.iloc[ind[i], 5] + gf_copy.iloc[ind[i] - 1, 5] + gf_copy.iloc[ind[i] - 2, 5] + \
                           gf_copy.iloc[ind[i] - 3, 5] + gf_copy.iloc[ind[i] - 4, 5] + gf_copy.iloc[ind[i] - 5, 5] + \
                           gf_copy.iloc[ind[i] - 6, 5]
            except:
                t[i] = 0
        return t

    gf["Stock-sum_7"] = stock_dif_sum(gf, index, stock_ticker)

    def result_of_strategy(table, ind, tick):
        gf_copy = table.copy(deep=True)
        t = gf_copy[tick].values
        for i in range(len(ind)):
            try:
                if gf_copy.iloc[ind[i] - 1, 6] < 0 and gf_copy.iloc[ind[i], 6] < -4 and gf_copy.iloc[
                    ind[i] - 1, 6] < -20 and gf_copy.iloc[
                    ind[i], 6] < -40:
                    t[i] = gf_copy.iloc[ind[i] + 1, 3]  # buy
                elif gf_copy.iloc[ind[i] - 1, 6] > 0 and gf_copy.iloc[ind[i], 6] > -4:
                    t[i] = gf_copy.iloc[ind[i] + 1, 3] * -1  # sell
                else:
                    t[i] = 0
            except:
                t[i] = 0

        return t

    #
    gf["Results"] = result_of_strategy(gf, index, stock_ticker)

    def signal_of_strategy(table, ind, tick):
        gf_copy = table.copy(deep=True)
        t = gf_copy[tick].values
        for i in range(len(ind)):
            try:
                if gf_copy.iloc[ind[i] - 1, 6] < 0 and gf_copy.iloc[ind[i], 6] < -4 and gf_copy.iloc[
                    ind[i] - 1, 6] < -20 and gf_copy.iloc[
                    ind[i], 6] < -40:
                    # t[i] = gf_copy.iloc[ind[i] + 1, 3]  # buy
                    t[i] = 1
                elif gf_copy.iloc[ind[i] - 1, 6] > 0 and gf_copy.iloc[ind[i], 6] > -4:
                    # t[i] = gf_copy.iloc[ind[i] + 1, 3] * -1  # sell
                    t[i] = 2
                else:
                    t[i] = 0
            except:
                t[i] = 0

        return t

    #
    gf["Signal"] = signal_of_strategy(gf, index, stock_ticker)

    return gf  # gf.nsmallest(1, stock_ticker), gf.nlargest(1, stock_ticker)


if __name__ == "__main__":
    # print(ts3(t1, t2))
    # print(ts2_minutes(t2))

    print(ts4(t1, t2))
