import numpy
import pandas as pd
import yfinance as yf
from pprint import pprint

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

class Yahoo_resp:
    def __init__(self, tick):
        self.y_tick = yf.Ticker(tick)

    def get_history(self, interval='1d'):
        hist = self.y_tick.history(start='2022-05-28', interval=interval)
        return hist

    def get_finanсials(self):
        fin = self.y_tick.financials
        return fin

    def get_quarterly_finansials(self):
        fin = self.y_tick.quarterly_financials
        return fin

    def cashflow(self):
        cf = self.y_tick.cashflow
        return cf


    def balance_sheet(self):
        bs = self.y_tick.balance_sheet
        return bs


    def q_balance_sheet(self):
        bs = self.y_tick.quarterly_balance_sheet
        return bs

    def sustainability(self):
        s = self.y_tick.sustainability
        return s

    def beta(self):
        s = self.y_tick.info['beta']
        return s

    def info(self):
        s = self.y_tick.info
        return s

# data = yf.download("SPY AAPL", start='2022-01-01', end='2022-04-30')

if __name__ == '__main__':
    # print(sustainability())
    # print(data)
    # pprint(info())
    # print(Yahoo_resp('AAPL').get_history(interval='1wk'))
    print(Yahoo_resp('AAPL').get_history())

