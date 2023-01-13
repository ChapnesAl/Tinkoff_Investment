import yfinance as yf
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


tick = "MSFT"
ticker = yf.Ticker(tick)

column1 = 'Total Assets'


df = ticker.balance_sheet.T

print(df)