from tinkoff.invest import Client, PortfolioResponse, RequestError, PortfolioPosition
import pandas as pd
import tokens
from dif_func.extra_func import from_figi_to_ticker

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def full_assets():
    with Client(tokens.test_token()) as client:
        a = client.operations.get_portfolio(account_id=tokens.id_test())
        # a = client.users.get_accounts().accounts
        print(a)


def general_assets():
    try:
        with Client(tokens.all_token_full()) as client:
            a = client.operations.get_portfolio(account_id=tokens.id_iss())
            # keys = ['total_amount_shares', 'total_amount_bonds', 'total_amount_etf', 'total_amount_currencies', 'total_amount_futures']
            # # print({getattr(a, k) for k in keys})
            # print(getattr(a, 'total_amount_shares'))
            # print({k: getattr(a, k) for k in keys})
            # y = getattr(a, 'total_amount_shares')
            # print(type(y))
            # x = pd.DataFrame([cast_money(getattr(a, k)) for k in keys], index=keys)
            # return x

            # df = pd.DataFrame([{
            #     'figi': p.figi,
            #     'quantity': cast_money(p.quantity),
            #     'expected_yield': cast_money(p.expected_yield),
            #     'instrument_type': p.instrument_type,
            #     'average_buy_price': cast_money(p.average_position_price),
            #     'currency': p.average_position_price.currency,
            #     'nkd': cast_money(p.current_nkd),
            # } for p in a.positions])
            # print(df.head(100))
            df = pd.DataFrame([portfolio_pose_todict(p) for p in a.positions])
            print(df.head(100))
            print(cast_money(a.total_amount_bonds), df.query("instrument_type == 'bond'")['sell_sum'].sum())
            print(round(df['commission'], 3).sum())
            # print(df['commission'].sum())

    except RequestError as e:
        print(str(e))


def portfolio_pose_todict(p: PortfolioPosition):
    r = {
        'figi': from_figi_to_ticker(p.figi),
        'quantity': cast_money(p.quantity),
        'expected_yield': cast_money(p.expected_yield),
        'instrument_type': p.instrument_type,
        'average_buy_price': cast_money(p.average_position_price),
        'currency': p.average_position_price.currency,
        'nkd': cast_money(p.current_nkd),
    }

    r['sell_sum'] = (r['average_buy_price']*r['quantity']) + r['expected_yield'] + (r['nkd']*r['quantity'])
    r['commission'] = r['sell_sum']*0.003
    r['tax'] = r['expected_yield']*0.013 if r['expected_yield'] > 0 else 0
    return r


def cast_money(v):
    return v.units + v.nano / 1e9


"""
Пока не работает:
    def cast_money(v):
        return v.units + v.nano / 1e9  # nano is 9 zero

"""

# MyAcc.full_assets(MyAcc)
if __name__ == '__main__':
    general_assets()
    # full_assets()

