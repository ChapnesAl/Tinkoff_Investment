from tinkoff.invest import Client, InstrumentStatus, Etf
import pandas as pd
import tokens
from pprint import pprint

pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def get_etfs():
    with Client(tokens.test_token()) as client:
        r = client.instruments.etfs(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_UNSPECIFIED)

        x = pd.DataFrame([some_column(s) for s in r.instruments])
        pprint(x)
    # return x


def get_companies():
    with Client(tokens.test_token()) as client:
        r = client.instruments.shares(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_BASE)
        df = pd.DataFrame([some_column(s) for s in r.instruments])
        # print(df)
    return df


def some_column(s):
    s = {
        'ticker': s.ticker,
        'name': s.name,
        'nominal': float('{:.3f}'.format(cast_money(s.nominal))),
        'sector': s.sector,
        'figi': s.figi,
        'class_code': s.class_code,
        'currency': s.currency,
        'short_enabled': s.short_enabled_flag,
        'api_trade': s.api_trade_available_flag,
        # 'exchange': s.exchange
    }
    return s
# ticker sector name currency nominal api_trade_available_flag  short_enabled_flag exchange

def cast_money(v):
    return v.units + v.nano / 1e9

if __name__ == '__main__':
    get_companies()
    # get_etfs()