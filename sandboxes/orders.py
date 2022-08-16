from tinkoff.invest import Client, OrderDirection, OrderType, Quotation
from tinkoff.invest.services import SandboxService
import tokens
import acc_id
import pandas as pd
from datetime import datetime
from pprint import pprint
from dif_func.order_book import better_bid, better_ask, last_bid

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


def buy_limit_order(figi, token):
    print('Песочница Тинькоф')

    with Client(tokens.sandbox_token()) as cl:
        sb: SandboxService = cl.sandbox

        r = sb.post_sandbox_order(
            figi=figi,
            quantity=1,
            price=better_bid(token, figi),
            account_id=acc_id.acc_a,
            order_id=datetime.now().strftime("%Y-%m-%dT %H:%M:%S"),
            direction=OrderDirection.ORDER_DIRECTION_BUY,
            order_type=OrderType.ORDER_TYPE_LIMIT
        )
        pprint(r)


def sell_limit_order(figi, token):
    print('Песочница Тинькоф')

    with Client(tokens.sandbox_token()) as cl:
        sb: SandboxService = cl.sandbox

        r = sb.post_sandbox_order(
            figi=figi,
            quantity=1,
            price=better_ask(token, figi),
            account_id=acc_id.acc_a,
            order_id=datetime.now().strftime("%Y-%m-%dT %H:%M:%S"),
            direction=OrderDirection.ORDER_DIRECTION_SELL,
            order_type=OrderType.ORDER_TYPE_LIMIT
        )
        pprint(r)

def get_active_orders(acc_id):
    print('Песочница Тинькоф')

    with Client(tokens.sandbox_token()) as cl:
        sb: SandboxService = cl.sandbox

        r = sb.get_sandbox_orders(account_id=acc_id).orders

        return r


def close_active_orders(acc_id):
    with Client(tokens.sandbox_token()) as cl:
        order = get_active_orders(acc_id)
        order_id = order[0].order_id
        print("Let's cancel order id %s" % order_id)
        r = cl.sandbox.cancel_sandbox_order(account_id=acc_id, order_id=order_id)

        print(r)






if __name__ == '__main__':
    # buy_limit_order('BBG000BSJK37', tokens.test_token())
    # sell_limit_order('BBG000BSJK37', tokens.test_token())
    close_active_orders(acc_id.acc_a)
    pprint(get_active_orders(acc_id.acc_a))