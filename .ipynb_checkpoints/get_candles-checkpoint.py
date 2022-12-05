from tinkoff.invest import Client, CandleInterval, RequestError, HistoricCandle
import pandas as pd
import tokens
from datetime import datetime, timedelta
from ta.trend import ema_indicator
import matplotlib.pyplot as plt


pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def graf_of_candles():
    try:
        with Client(tokens.test_token()) as client:
            r = client.market_data.get_candles(
                figi='FUTSBRF09220',
                from_=datetime.utcnow() - timedelta(days=365),
                to=datetime.utcnow(),
                interval=CandleInterval.CANDLE_INTERVAL_DAY
            )
            df = create_df(r.candles)
            # # df['ema'] = ema_indicator(close=df['close'], window=9)
            # print(df[['time', 'close']])
            # ax=df.plot(x='time', y='close')
            # df.plot(ax=ax, x='time', y='close')
            # plt.show()
            return print(df)
    except RequestError as e:
        print(str(e))

def graf_of_candles():
    try:
        with Client(tokens.test_token()) as client:
            r = client.market_data.get_candles(
                figi='USD000UTSTOM',
                from_=datetime.utcnow() - timedelta(days=7),
                to=datetime.utcnow(),
                interval=CandleInterval.CANDLE_INTERVAL_HOUR
            )
            df = create_df(r.candles)
            df['ema'] = ema_indicator(close=df['close'], window=9)
            print(df[['time', 'close', 'ema']].tail(30))
            ax=df.plot(x='time', y='close')
            df.plot(ax=ax, x='time', y='ema')
            plt.show()

    except RequestError as e:
        print(str(e))


def create_df(candles: [HistoricCandle]):
    df = pd.DataFrame([{
        'time': c.time,
        'volume': c.volume,
        'open': cast_money(c.open),
        'close': cast_money(c.close),
        'high': cast_money(c.high),
        'low': cast_money(c.low),
    } for c in candles])
    return df



def cast_money(v):
    return v.units + v.nano / 1e9

if __name__ == '__main__':
    graf_of_candles()