from tinkoff.invest import Client
from pprint import pprint
import pandas as pd
from tokens import test_token, id_test
from dif_func.often_use import cast_money


def order_book(token, figi):

    with Client(token) as client:
        book = client.market_data.get_order_book(figi=figi, depth=50)

        bids = [cast_money(p.price) for p in book.bids]
        asks = [cast_money(p.price) for p in book.asks]

    return bids, asks

def spread_ob(token, figi):

    a = order_book(token, figi)
    b = min(a[1]) - max(a[0])
    c = b / (min(a[1]) / 100)
    return float('{:.3f}'.format(c))

def better_ask(token, figi):

    with Client(token) as client:
        book = client.market_data.get_order_book(figi=figi, depth=50)

        a = cast_money(book.asks[0].price)

        return a


def better_bid(token, figi):

    with Client(token) as client:
        book = client.market_data.get_order_book(figi=figi, depth=50)

        a = cast_money(book.bids[0].price)

        return a

def last_bid(token, figi):

    with Client(token) as client:
        book = client.market_data.get_order_book(figi=figi, depth=50)

        a = cast_money(book.bids[-1].price)

        return a


if __name__ == '__main__':
    print(order_book(test_token(), 'BBG000BSJK37'))
    # print(spread_ob(test_token(), 'BBG0013HGFT4'))
    print(better_ask(test_token(), 'BBG000BSJK37'))
    # print(better_bid(test_token(), 'BBG000BSJK37'))