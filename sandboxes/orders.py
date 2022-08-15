from tinkoff.invest import Client, OrderDirection, OrderType
from tinkoff.invest.services import SandboxService
import tokens
import acc_id
import pandas as pd
from datetime import datetime
from pprint import pprint

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

fiqi = 'BBG004730N88' # SBER

def buy_order():
    print('Песочница Тинькоф')

    with Client(tokens.sandbox_token()) as cl:
        sb: SandboxService = cl.sandbox

        r = sb.post_sandbox_order(
            figi=fiqi,
            quantity=1,
            account_id=acc_id.acc_a,
            order_id=datetime.now().strftime("%Y-%m-%dT %H:%M:%S"),
            direction=OrderDirection.ORDER_DIRECTION_BUY,
            order_type=OrderType.ORDER_TYPE_MARKET
        )
        pprint(r)

def sell_order():
    print('Песочница Тинькоф')

    with Client(tokens.sandbox_token()) as cl:
        sb: SandboxService = cl.sandbox

        r = sb.post_sandbox_order(
            figi=fiqi,
            quantity=1,
            account_id=acc_id.acc_a,
            order_id=datetime.now().strftime("%Y-%m-%dT %H:%M:%S"),
            direction=OrderDirection.ORDER_DIRECTION_SELL,
            order_type=OrderType.ORDER_TYPE_MARKET
        )
        pprint(r)


def buy_limit_order():
    print('Песочница Тинькоф')

    with Client(tokens.sandbox_token()) as cl:
        sb: SandboxService = cl.sandbox

        r = sb.post_sandbox_order(
            figi=fiqi,
            quantity=1,
            price=160,
            account_id=acc_id.acc_a,
            order_id=datetime.now().strftime("%Y-%m-%dT %H:%M:%S"),
            direction=OrderDirection.ORDER_DIRECTION_BUY,
            order_type=OrderType.ORDER_TYPE_LIMIT
        )
        pprint(r)


if __name__ == '__main__':
    sell_order()