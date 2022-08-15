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

    return(bids, asks)


if __name__ == '__main__':
    print(order_book(test_token(),'BBG0013HGFT4'))