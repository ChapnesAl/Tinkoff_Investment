from yahoo_fin.stock_info import get_data, get_income_statement
import yahoo_fin.stock_info as si
import pandas as pd


income_statement = si.get_income_statement("aapl")
print(income_statement)



# https://finance.yahoo.com/quote/aapl/financials?p=aapl
#             ""