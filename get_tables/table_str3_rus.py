from tinkoff.invest import Client, CandleInterval, RequestError, HistoricCandle
import pandas as pd
import tokens
from datetime import datetime, timedelta
import numpy
from ta.trend import ema_indicator
import matplotlib.pyplot as plt


pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# figi1 = 'BBG004S68B31'     #'FUTSBRF09220'
stock_ticker = 'TTT'

x = ['BBG004S68B31', 'MOEX']

def ts3_rus(figi, stock_ticker):

    def graf_of_candles(fiqi):
        try:
            with Client(tokens.test_token()) as client:
                r = client.market_data.get_candles(
                    figi=fiqi,
                    from_=datetime.utcnow() - timedelta(days=365),
                    to=datetime.utcnow(),
                    interval=CandleInterval.CANDLE_INTERVAL_DAY
                )
                df = create_df(r.candles)

            return df
        except RequestError as e:
            print(str(e))




    def create_df(candles: [HistoricCandle]):
        df = pd.DataFrame([{
            # 'time': c.time,
            # 'volume': c.volume,
            # 'open': cast_money(c.open),
            'close': cast_money(c.close),
            # 'high': cast_money(c.high),
            # 'low': cast_money(c.low),
        } for c in candles])
        return df



    def cast_money(v):
        return v.units + v.nano / 1e9

    df = pd.DataFrame()
    df[f"{stock_ticker}"] = graf_of_candles(figi)

    def add_percent_update(df, tick):
        """ day to day stock's or market's update"""
        df_copy = df.copy(deep=True)
        df_copy = pd.DataFrame(df_copy.drop(df.index[0]))
        df_copy_v = df_copy[tick].values
        df_v = df.copy(deep=True)
        df_vv = df_v[tick].values

        for i in range(len(df_copy)):
            df_vv[i] = (df_copy_v[i] - df_vv[i]) / (df_vv[i] / 100)

        df_vv = numpy.insert(df_vv, 0, 0)
        df_vv = numpy.delete(df_vv, -1)
        return df_vv


    df[f"% update {stock_ticker}"] = add_percent_update(df, stock_ticker)


    def get_index(table):
        gf_copy = table.copy(deep=True)
        gf_copy = gf_copy.reset_index()
        gf_copy = gf_copy.index.tolist()
        return gf_copy


    index = get_index(df)


    def add_week_difference(table, ind):
        """ Sum of date stock's update"""
        gf_copy = table.copy(deep=True)
        gf_copy2 = table.copy(deep=True)
        t = gf_copy2.iloc[:, 1]
        for i in range(len(ind)):
            try:
                # 7 days
                if gf_copy.iloc[ind[i], 1] in [gf_copy.iloc[0, 1], gf_copy.iloc[1, 1], gf_copy.iloc[2, 1],
                                               gf_copy.iloc[3, 1], gf_copy.iloc[4, 1], gf_copy.iloc[5, 1],
                                               gf_copy.iloc[6, 1]]:
                    t[i] = 0
                else:
                    t[i] = (gf_copy.iloc[ind[i], 1] + gf_copy.iloc[ind[i] - 1, 1] + gf_copy.iloc[ind[i] - 2, 1] +
                            gf_copy.iloc[ind[i] - 3, 1] + gf_copy.iloc[ind[i] - 4, 1] + gf_copy.iloc[ind[i] - 5, 1] +
                            gf_copy.iloc[ind[i] - 6, 1])
            except:
                t[i] = 0
        return t


    df["Week differ Stock"] = add_week_difference(df, index)


    def signal_to_deal(table, ind, tick):
        """ Long and Short"""
        gf_copy = table.copy(deep=True)
        gf_copy = gf_copy.astype({tick: str}, errors='ignore')
        r = gf_copy[tick].values

        for i in range(len(ind)):
            try:

                if gf_copy.iloc[ind[i], 2] > 0 and gf_copy.iloc[ind[i], 2] < 2 \
                        and gf_copy.iloc[ind[i] - 1, 2] > 2.5 and gf_copy.iloc[ind[i] - 1, 2] < 10 \
                        and gf_copy.iloc[ind[i] - 2, 2] > 5 and gf_copy.iloc[ind[i] - 2, 2] < 10 \
                        and gf_copy.iloc[ind[i] - 3, 2] > 0 and gf_copy.iloc[ind[i] - 3, 2] < 25 \
                        and gf_copy.iloc[ind[i] - 4, 2] > 0 and gf_copy.iloc[ind[i] - 4, 2] < 20 \
                        and gf_copy.iloc[ind[i] - 5, 2] < 20:
                    r[i] = 'Short'  # buy
                    # r[i] = 1  # buy
                elif gf_copy.iloc[ind[i], 2] < 0 and gf_copy.iloc[ind[i], 2] > -2 \
                        and gf_copy.iloc[ind[i] - 1, 2] < -2.5 and gf_copy.iloc[ind[i] - 1, 2] > -30 \
                        and gf_copy.iloc[ind[i] - 2, 2] < 5 and gf_copy.iloc[ind[i] - 2, 2] > -40 \
                        and gf_copy.iloc[ind[i] - 3, 2] < -1 and gf_copy.iloc[ind[i] - 3, 2] > -30 \
                        and gf_copy.iloc[ind[i] - 4, 2] < 10:
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
    #             if gf_copy.iloc[ind[i], 2] < 0 and gf_copy.iloc[ind[i], 2] > -2 \
    #                     and gf_copy.iloc[ind[i] - 1, 2] < -2.5 and gf_copy.iloc[ind[i] - 1, 2] > -30 \
    #                     and gf_copy.iloc[ind[i] - 2, 2] < 5 and gf_copy.iloc[ind[i] - 2, 2] > -40 \
    #                     and gf_copy.iloc[ind[i] - 3, 2] < -1 and gf_copy.iloc[ind[i] - 3, 2] > -30 \
    #                     and gf_copy.iloc[ind[i] - 4, 2] < 10:
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


    df["Signal"] = signal_to_deal(df, index, stock_ticker)


    # print(gf)

    def result_of_strategy(table, ind, tick):
        gf_copy = table.copy(deep=True)
        t = gf_copy[tick].values
        for i in range(len(ind)):
            try:
                if gf_copy.iloc[ind[i], 3] == 'Long':
                    t[i] = gf_copy.iloc[ind[i] + 1, 1]  # buy
                elif gf_copy.iloc[ind[i], 3] == 'Short':
                    t[i] = gf_copy.iloc[ind[i] + 1, 1] * -1  # sell
                else:
                    t[i] = 0
            except:
                t[i] = 0

        return t


    #
    df["Results"] = result_of_strategy(df, index, stock_ticker)

    return df

if __name__ == '__main__':
    print(ts3_rus(x[0], x[1]))

    # print(graf_of_candles(figi1))