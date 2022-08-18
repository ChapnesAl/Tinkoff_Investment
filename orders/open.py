from tickers import snp_b_15, snp_b_15a, snp_b_15b, snp_b_15c, snp_b_15d, snp_b_15e
from tickers import b_15_plus, b_15_plus_a, b_15_plus_b, b_15_plus_c, b_15_plus_d, b_15_plus_e
from result_mdl.play_ground_str4 import Str4_0_0, Str4_1_1, Str4_2_2
import pandas as pd
from dif_func.yahoo_requests import Yahoo_resp

def get_beta(market, stock, s_time, f_time=None, interval='1d'):
    df = Str4_2_2(market, stock, stime=s_time, ftime=f_time, interval=interval).signals_without_gap()
    df_copy = df.copy(deep=True)
    tickers = df_copy['Companies'].values
    for i in range(len(tickers)):
        tickers[i] = Yahoo_resp(tickers[i]).beta()
    df['beta'] = tickers

    return df

df = get_beta('^GSPC', ['AAPL','GPS'], '2022-01-01', '2022-08-15', interval='1wk')

def get_split():
    x = 0

if __name__ == '__main__':
    print(get_beta('^GSPC', ['AAPL','GPS'], '2022-01-01', '2022-08-15', interval='1wk'))
