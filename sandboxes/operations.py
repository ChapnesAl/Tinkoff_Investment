from tinkoff.invest import Client, OrderDirection, OrderType, Quotation
from tinkoff.invest.services import SandboxService
import tokens
import acc_id
from datetime import datetime
import pandas as pd
from pprint import pprint



def get_sb_operations():
    print('Песочница Тинькоф')

    with Client(tokens.sandbox_token()) as cl:
        sb: SandboxService = cl.sandbox

        a = sb.get_sandbox_operations(
                account_id=acc_id.acc_a,
                from_=datetime(2022, 5, 1),
                to=datetime.utcnow()
                )
        pprint(a)


if __name__ == '__main__':
    get_sb_operations()