from datetime import datetime

from tokens import test_token, id_test
from tinkoff.invest import Client, InstrumentStatus, InstrumentIdType, OperationState, RequestError
import pandas as pd
from pprint import pprint




def from_ticker_to_figi(ticker, class_code):
    with Client(test_token()) as client:
        a = client.instruments.get_instrument_by(id=ticker, id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_TICKER,
                                                 class_code=class_code)
        b = getattr(getattr(a, 'instrument'), 'figi')
        return b


def from_figi_to_ticker(figi):
    with Client(test_token()) as client:
        a = client.instruments.get_instrument_by(id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI, id=figi)
        b = getattr(getattr(a, 'instrument'), 'ticker')
        return b

def about_futures():
    with Client(test_token()) as client:
        a = client.instruments.futures(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_BASE)
        return a

def get_time_of_market():
    with Client(test_token()) as client:
        a = client.instruments.trading_schedules(
            # exchange=
            from_=datetime.utcnow(),
            to=datetime(2022, 7, 15), # time to more than 7 days
        )
        return a

def my_operations():
    try:
        with Client(test_token()) as client:
            a = client.operations.get_operations(
                account_id=id_test(),
                from_=datetime(2021, 1, 1),
                to=datetime.utcnow()
                # figi='BBB'
                # state=OperationState.OPERATION_STATE_CANCELED # operations with deals which I didn't open + can change this parametr
            )
    except RequestError as e:
        print(str(e))
    return a


# figi='FUTSPYF09220',
# ticker='SFU2',
# class_code='SPBFUT'
# pprint(about_futures())




# class Database:
#     def __init__(self, db_file):
#         self.connection = sq.connect(db_file)
#         self.cursor = self.connection.cursor()
#
#     def user_exists(self, user_id):  # with this function we are finding a user and get boolean value
#         with self.connection:
#             result = self.cursor.execute("SELECT * FROM users WHERE `user_id` = ?",
#                                          (user_id,)).fetchall()  # fetchall = get all values
#             return bool(len(result))
#
#     def add_user(self, user_id):  # with this function we are adding users
#         with self.connection:
#             return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
#
#     def user_money(self, user_id):  # get information about current user's money
#         with self.connection:
#             result = self.cursor.execute("SELECT `money` FROM users WHERE `user_id` = ?", (user_id,)).fetchmany(


if __name__ == '__main__':
    print(from_figi_to_ticker('BBG0013HGFT4'))



# 0  BBG0013HGFT4        currency  100000.0
# 1  FG0000000000        currency   -1250.0
# 2  BBG004730N88           share      10.0