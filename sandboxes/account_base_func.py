from tinkoff.invest import Client, MoneyValue, PortfolioPosition
from tinkoff.invest.services import SandboxService
import tokens
import acc_id
import pandas as pd

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


class AccPortfolio():

    def __init__(self, acc_id):
        self.acc = acc_id

    def get_acc_portfolio(self):
        print('Песочница Тинькоф')

        with Client(tokens.sandbox_token()) as cl:
            sb: SandboxService = cl.sandbox
            a = sb.get_sandbox_portfolio(account_id=self.acc)

            r = pd.DataFrame(self.operations_todict(s) for s in a.positions)

            # r = a[0]

            return print(r)

    def operations_todict(self, p : PortfolioPosition):
        r = {
            'figi': p.figi,
            'instrument_type': p.instrument_type,
            'quantity': float('{:.3f}'.format(self.cast_money(p.quantity))),
            'average_position_price': float('{:.3f}'.format(self.cast_money(p.average_position_price))),
            'expected_yield': float('{:.3f}'.format(self.cast_money(p.expected_yield))),
            'current_nkd ': float('{:.3f}'.format(self.cast_money(p.current_nkd))),
            'average_position_price_pt': float('{:.3f}'.format(self.cast_money(p.average_position_price_pt))),
            'current_price': float('{:.3f}'.format(self.cast_money(p.current_price))),
            # 'api_trade': s.api_trade_available_flag,
            # 'average_position_price_fifo': s.api_trade_available_flag,
            # 'quantity_lots': s.api_trade_available_flag,
        }
        return r

    def cast_money(self, v):
        return v.units + v.nano / 1e9






def pay_in(acc_id):
    print('Песочница Тинькоф')

    with Client(tokens.sandbox_token()) as cl:
        sb: SandboxService = cl.sandbox

        r = sb.sandbox_pay_in(account_id=acc_id,
                              amount=MoneyValue(units=100000, nano=000000000, currency='usd'))

        print(r)




if __name__ == '__main__':
    # get_acc_portfolio(acc_id.acc_a)
    AccPortfolio(acc_id.acc_a).get_acc_portfolio()
    # pay_in(acc_id.acc_a)