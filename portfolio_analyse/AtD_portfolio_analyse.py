from about_acc import get_portfolio_usd_tickers
import fundamentalanalysis as fa
import numpy as np
import pandas as pd
import yfinance as yf
import datetime
from dateutil.relativedelta import relativedelta



api_key = '00ef9804fcde0edd93b1b4821ee2f06a'
# api_key = 'c81352430e2fe3c941faf0814227562b'

''' крайний год для анализа'''
required_year = '2022'

''' время '''
stime='2015-01-01'
period = '1mo'  # '1d' '1wk'


def change_percent_all_columns(df):
    x = df.columns.to_list()
    for i in range(len(x)):
        v = df[x[i]].to_list()
        l = []
        for y in range(len(v)):
            try:
                if y != len(v):
                    if v[y] < 0 and v[y+1] > 0:
                        l.append('Minus')
                    elif v[y] > 0 and v[y+1] < 0:
                        l.append('Plus')
                    else:
                        vv = (v[y] / (v[y+1] / 100)) - 100
                        l.append(vv)
                else:
                    vv = 0
                    l.append(vv)
                    # print(vv)
            except:
                l.append(0)
        df[f'change % {x[i]}'] = l
    return df


def one_stock_analyse(ticker, api_key, required_year):
    ''' запрос к yahoo за ценами '''

    def get_data_from_ticker(tick, start_time='2017-01-01', interval='1mo'):
        ticker = yf.Ticker(tick)

        df = ticker.history(start=start_time, end=None, interval=interval)
        x = pd.DataFrame(df)
        x.rename(columns={"Close": tick}, inplace=True)
        z = x.drop(columns=["Open", "High", "Low", "Volume", "Dividends", "Stock Splits"])
        return z

    df = get_data_from_ticker(ticker)

    ''' получаем цену на период отчета '''
    income_statement = fa.income_statement(ticker, api_key)
    accepted_date = income_statement.T['acceptedDate'][0][:10]
    df_report = get_data_from_ticker(ticker, accepted_date)
    report_price = df_report.iloc[0, 0]

    ''' получаем актуальную цену акции '''
    today = datetime.date.today()
    sdate = today - relativedelta(months=3)
    sdate = str(sdate)
    df_current_price = get_data_from_ticker(ticker, sdate, '1d')
    current_price = df_current_price.iloc[-1, 0]

    ''' меняем индекс для корреляции с df ключевых метрик '''

    def change_index(df):
        df_index = df.index.to_list()
        for i in range(len(df_index)):
            t = df_index[i].date()
            df_index[i] = t.strftime('%Y-%m-%d')
        df['Date_index'] = df_index
        df = df.set_index('Date_index')
        return df

    df = change_index(df)

    def get_key_metricks(ticker, api_key, required_year):
        key_metrics = fa.key_metrics(ticker, api_key, period='annual')
        df_key_metr = key_metrics.T
        df_key_metr = df_key_metr.loc[required_year:'2000'].copy(deep=True)
        return df_key_metr

    df_key_metr = get_key_metricks(ticker, api_key, required_year)

    if df_key_metr.index[0] == required_year and f'{int(required_year) + 1}-01-01' in df.index.to_list():
        last_year = True
    else:
        last_year = False

    def get_index(df):
        index_years = df.index.to_list()
        return index_years

    index_years = get_index(df_key_metr)

    def get_price_from_df(df, list_dates):
        new_list = []
        for i in range(len(list_dates)):
            x = int(list_dates[i])
            x += 1
            x = str(x)
            try:
                r = df.loc[f'{x}-01-01']
                r = float(r)
                new_list.append(r)
            except:
                new_list.append(0)

        return new_list

    stock_year_prices = get_price_from_df(df, index_years)

    df_key_metr[ticker] = list(stock_year_prices)
    df_key_metr.drop('period', axis=1, inplace=True)

    def change_percent_all_columns(df):
        x = df.columns.to_list()
        for i in range(len(x)):
            v = df[x[i]].to_list()
            l = []
            for y in range(len(v)):
                try:
                    if y != len(v):
                        vv = (v[y] / (v[y + 1] / 100)) - 100
                        l.append(vv)
                    else:
                        vv = 0
                        l.append(vv)
                except:
                    l.append(0)
            df[f'change % {x[i]}'] = l
        return df

    df_with_changes = change_percent_all_columns(df_key_metr)

    # if df_with_changes[f'change % {ticker}'][0] > df_with_changes[f'change % {ticker}'][1] and df_with_changes['change % debtToAssets'][0] < df_with_changes['change % debtToAssets'][1]:
    #     better_less_last = "Short"
    if df_with_changes[f'change % {ticker}'][0] < df_with_changes[f'change % {ticker}'][1] and \
            df_with_changes['change % debtToAssets'][0] > df_with_changes['change % debtToAssets'][1] and \
            df_with_changes['change % debtToAssets'][0] > df_with_changes[f'change % {ticker}'][0]:
        better_less_last = "Long"
    else:
        better_less_last = False

    change_price = current_price / (report_price / 100) - 100

    if last_year == True and better_less_last != False:
        # df_last = df_with_changes.reindex(index=df_with_changes.index[::-1])
        r = [ticker, accepted_date, report_price, current_price, change_price,
             df_with_changes['change % debtToAssets'][0], better_less_last]
    else:
        r = None

    return r


def get_results_da_price(tickers_list, api_key, required_year):
    l = []
    for i in range(len(tickers_list)):
        r = one_stock_analyse(tickers_list[i], api_key, required_year)
        if r == None:
            pass
        else:
            l.append(r)
    return l


portfolio = get_portfolio_usd_tickers()

df = pd.DataFrame(get_results_da_price(portfolio, api_key, required_year),
                  columns=['Ticker', 'Accepted_Date', 'Price', 'Current Price', 'Change % price',
                           'change % debtToAssets', 'Side'])


if __name__ == '__main__':
    print(df)
    print(portfolio)