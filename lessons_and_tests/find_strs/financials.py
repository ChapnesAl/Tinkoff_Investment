import yfinance as yf
import pandas as pd
import numpy as np
import fundamentalanalysis

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


from pandas_datareader import data as pdr





tick = "MSFT"
ticker = yf.Ticker(tick)

column1 = 'Total Assets'


df = ticker.balance_sheet.T

pdr

print(df)