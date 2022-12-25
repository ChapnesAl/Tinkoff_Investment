import pandas as pd
from tokens import iss_token_full
from sql_investi.sql_str_tests import Db_str_tests
from strategies.working_str.str100.w_play_ground_str1 import Str1_0_0
from strategies.working_str.str100.w_play_ground_str1 import Cr_Str1_0_0
from sql_investi.sql_str_tests import Db_str_tests



pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

mt = '^GSPC'  # '^GSPC', '^IXIC', '^RUT', '^DJI'
st = 'T'

snp_b_15 = ['COTY', 'CCL', 'JWN', 'DXC', 'HAL', 'SLB', 'RCL', 'BFH', 'DVN', 'OXY', 'WYNN', 'PVH', 'GPS', 'XRX', 'BKR',
            'PARA', 'FCX', 'ALK', 'WDC', 'C', 'MOS', 'OKE', 'DHI', 'BBY', 'MPC', 'AMD', 'PRU', 'EXPE', 'EOG', 'VLO',
            'MAR', 'HCA', 'ALB']
snp_b_15_2 = ['GPS', 'XRX', 'BKR', 'PARA', 'FCX', 'ALK', 'WDC', 'C', 'MOS', 'OKE', 'DHI', 'BBY', 'MPC', 'AMD', 'PRU', 'EXPE', 'EOG', 'VLO', 'MAR', 'HCA', 'ALB']

snp_b_13_15 = ['KEY', 'BAC', 'LVS', 'UAL', 'HOG', 'CFG', 'ALK', 'MAS', 'BBY', 'EMR', 'PSX', 'MS', 'LYB', 'RTX', 'RL', 'COP', 'AMAT', 'QRVO', 'SPG', 'DRI', 'BA', 'META', 'NVDA', 'FDX', 'ADSK', 'ABMD', 'GS']

snp_b_09_11 = ['F', 'WU', 'KMI', 'CNP', 'HPQ', 'GLW', 'KHC', 'LUV', 'CMCSA', 'NRG', 'BK', 'CSCO', 'USB', 'TJX', 'CAH', 'HIG', 'SCHW', 'HAS', 'WELL', 'DXCM', 'ROST', 'GRMN', 'NKE', 'YUM', 'GOOGL', 'JPM', 'GOOG', 'GPN', 'MMM', 'AXP', 'TGT', 'TXN', 'CRM', 'NDAQ', 'CAT', 'ILMN', 'V', 'GD', 'NFLX', 'MSFT', 'HD', 'MA', 'SPGI', 'IDXX', 'ADBE', 'AVGO']

snp_b_11_13 = ['UAA', 'HBAN', 'HPE', 'IVZ', 'KEY', 'RF', 'BEN', 'WMB', 'DAL', 'GM', 'WRK', 'WFC', 'EBAY', 'VTR', 'AIG', 'MU', 'MET', 'NTAP', 'SYY', 'BXP', 'MNST', 'XOM', 'PYPL', 'DIS', 'TROW', 'HLT', 'QCOM', 'CVX', 'AAPL', 'HON', 'UPS', 'LOW', 'ACN', 'SNPS', 'LRCX', 'BKNG']

snp_more_b2 = ['COTY', 'CCL', 'JWN', 'DXC', 'HAL', 'SLB', 'RCL', 'BFH', 'DVN', 'OXY', 'WYNN', 'PVH']

more_stocks = ['EHTH', 'CCL', 'UAA', 'GPS', 'MAC', 'PUMP', 'ACH', 'ET', 'VIPS', 'PLTR', 'PTON', 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD',  'SHI', 'IVZ', 'M', 'WU', 'M', 'CNK', 'KMI', 'TRIP', 'LEVI', 'KEY', 'CHX', 'IBN', 'CHGG', 'RF', 'WB', 'JWN', 'LTHM', 'PINS', 'ANAB', 'T', 'UPWK', 'UBER', 'VREX', 'BJRI', 'BILI', 'SAVE', 'BEN', 'PARA', 'YY', 'FCX', 'BKR', 'RRC', 'TTM', 'HAL', 'CNP', 'SMAR', 'DXC', 'PPC', 'EVC', 'WMB', 'HPQ', 'DAL', 'USFD', 'BAC', 'APA', 'CLW', 'SLB', 'HOG', 'SPR', 'GM', 'PLAY', 'SAGE', 'BYND', 'LVS', 'Z', 'NRG', 'RCL', 'BSX', 'CFG', 'LI', 'WBA', 'KHC', 'EQT', 'CHEF', 'TWTR', 'INTC', 'TDOC', 'IRBT', 'WRK', 'UAL', 'LUV', 'BTI' , 'BFH', 'IRBT', 'BK', 'ALK', 'CMCSA', 'WFC', 'MO', 'ARWR', 'EQT', 'CSCO', 'VZ', 'KR', 'TTD', 'NEM', 'EBAY', 'AYX', 'IRM', 'PTR', 'NET', 'USB', 'CPRI', 'WDC', 'OVV', 'SNY', 'W', 'PFGC', 'MOS', 'TTE', 'AIG', 'C', 'VTR', 'DOW', 'MAS', 'BUD', 'NVAX', 'CAH', 'SIG', 'COIN', 'DVN', 'PVH', 'OKE', 'TJX', 'GILD', 'MET', 'REGI', 'MU', 'OXY', 'MDLZ', 'KO', 'JD', 'WYNN', 'EIX', 'DOCU', 'SCHW', 'HIG', 'CLR', 'OMC', 'NTAP', 'MTCH', 'BALL', 'BBY', 'SO', 'SQ', 'BMY', 'ORCL', 'HAS', 'STX', 'DHI', 'ROST', 'D', 'ADM', 'ATVI', 'INCY', 'FSLR', 'NEE', 'SBUX', 'MS', 'H', 'TWLO']

snp_more_b_09 = ['F', 'WU', 'KMI', 'CNP', 'HPQ', 'GLW', 'KHC', 'LUV', 'CMCSA', 'NRG', 'BK', 'CSCO', 'USB', 'TJX', 'CAH', 'HIG', 'SCHW', 'HAS', 'WELL', 'DXCM', 'ROST', 'GRMN', 'NKE', 'YUM', 'GOOGL', 'JPM', 'GOOG', 'GPN', 'MMM', 'AXP', 'TGT', 'TXN', 'CRM', 'NDAQ', 'CAT', 'ILMN', 'V', 'GD', 'NFLX', 'MSFT', 'HD', 'MA', 'SPGI', 'IDXX', 'ADBE', 'AVGO',
'UAA', 'HBAN', 'HPE', 'IVZ', 'KEY', 'RF', 'BEN', 'WMB', 'DAL', 'GM', 'WRK', 'WFC', 'EBAY', 'VTR', 'AIG', 'MU', 'MET', 'NTAP', 'SYY', 'BXP', 'MNST', 'XOM', 'PYPL', 'DIS', 'TROW', 'HLT', 'QCOM', 'CVX', 'AAPL', 'HON', 'UPS', 'LOW', 'ACN', 'SNPS', 'LRCX', 'BKNG',
'KEY', 'BAC', 'LVS', 'UAL', 'HOG', 'CFG', 'ALK', 'MAS', 'BBY', 'EMR', 'PSX', 'MS', 'LYB', 'RTX', 'RL', 'COP', 'AMAT', 'QRVO', 'SPG', 'DRI', 'BA', 'META', 'NVDA', 'FDX', 'ADSK', 'ABMD', 'GS',
'GPS', 'XRX', 'BKR', 'PARA', 'FCX', 'ALK', 'WDC', 'C', 'MOS', 'OKE', 'DHI', 'BBY', 'MPC', 'AMD', 'PRU', 'EXPE', 'EOG', 'VLO', 'MAR', 'HCA', 'ALB',
'COTY', 'CCL', 'JWN', 'DXC', 'HAL', 'SLB', 'RCL', 'BFH', 'DVN', 'OXY', 'WYNN', 'PVH']

snp_b_09_2 = ['F', 'WU', 'KMI', 'CNP', 'HPQ', 'GLW', 'KHC', 'LUV', 'CMCSA', 'NRG', 'BK', 'CSCO', 'USB', 'TJX', 'CAH', 'HIG', 'SCHW', 'HAS', 'WELL', 'DXCM', 'ROST', 'GRMN', 'NKE', 'YUM', 'GOOGL', 'JPM', 'GOOG', 'GPN', 'MMM', 'AXP', 'TGT', 'TXN', 'CRM', 'NDAQ', 'CAT', 'ILMN', 'V', 'GD', 'NFLX', 'MSFT', 'HD', 'MA', 'SPGI', 'IDXX', 'ADBE', 'AVGO',
'UAA', 'HBAN', 'HPE', 'IVZ', 'KEY', 'RF', 'BEN', 'WMB', 'DAL', 'GM', 'WRK', 'WFC', 'EBAY', 'VTR', 'AIG', 'MU', 'MET', 'NTAP', 'SYY', 'BXP', 'MNST', 'XOM', 'PYPL', 'DIS', 'TROW', 'HLT', 'QCOM', 'CVX', 'AAPL', 'HON', 'UPS', 'LOW', 'ACN', 'SNPS', 'LRCX', 'BKNG',
'KEY', 'BAC', 'LVS', 'UAL', 'HOG', 'CFG', 'ALK', 'MAS', 'BBY', 'EMR', 'PSX', 'MS', 'LYB', 'RTX', 'RL', 'COP', 'AMAT', 'QRVO', 'SPG', 'DRI', 'BA', 'META', 'NVDA', 'FDX', 'ADSK', 'ABMD', 'GS',
'GPS', 'XRX', 'BKR', 'PARA', 'FCX', 'ALK', 'WDC', 'C', 'MOS', 'OKE', 'DHI', 'BBY', 'MPC', 'AMD', 'PRU', 'EXPE', 'EOG', 'VLO', 'MAR', 'HCA', 'ALB']



coin_new_popular = ['MATIC-USD', 'WTRX-USD', 'DOT-USD', 'SHIB-USD', 'SOL-USD', 'HEX-USD', 'STETH-USD', 'UNI7083-USD', 'AVAX-USD', 'LEO-USD', 'TON11419-USD']


""" Str 1 0 0"""




def for_test(slist):
    s1 = list(slist)
    s2 = list(slist)
    s3 = list(slist)
    s4 = list(slist)
    s5 = list(slist)
    s6 = list(slist)
    a = Str1_0_0('^GSPC', s1, stime='2018-05-01', ftime='2020-01-01', interval='1wk').sum_results()
    b = Str1_0_0('^GSPC', s2, stime='2019-05-01', ftime='2020-06-01', interval='1wk').sum_results()
    c = Str1_0_0('^GSPC', s3, stime='2019-10-01', ftime='2021-01-01', interval='1wk').sum_results()
    d = Str1_0_0('^GSPC', s4, stime='2020-05-01', ftime='2021-10-01', interval='1wk').sum_results()
    e = Str1_0_0('^GSPC', s5, stime='2021-06-01', ftime='2022-04-03', interval='1wk').sum_results()
    f = Str1_0_0('^GSPC', s6, stime='2022-01-01', interval='1wk').sum_results()

    return a, b, c, d, e, f


# def pack_analyse(slist):
#     l = list(pack_st_op)
#     for i in range(len(pack_st_op)):
#         l[i] = for_test(slist, pack_st_op[i])
#     return tuple(l)


if __name__ == '__main__':


    ''' STOCKS - chose first day as ftime of a new week for a signal week'''
    # print(Str1_0_0('^GSPC', snp_more_b_09).signals())
    # print(Str1_0_0('^GSPC', snp_b_09_11).signals())
    # print(Str1_0_0('^GSPC', snp_b_11_13).signals())
    # print(Str1_0_0('^GSPC', snp_b_13_15).signals())
    # print(Str1_0_0('^GSPC', snp_b_15_2).signals())
    # print(Str1_0_0('^GSPC', snp_more_b2).signals())
    # print(Str1_0_0('^GSPC', 'F').get_table())

    # print(Str1_0_0('^GSPC', snp_more_b_09, stime='2021-05-01', ftime='2022-12-16').signals())
    # print(Str1_0_0('^GSPC', snp_more_b_09, stime='2021-05-01').signals())
    # print(Str1_0_0('^GSPC', 'F', stime='2021-05-01', ftime='2022-12-10').get_table())
    print(Str1_0_0('^GSPC', 'HPE', stime='2021-05-01').get_table())

    ''' CRYPTO - chose first day as ftime of a new week for a signal week'''
    # print(Cr_Str1_0_0('BTC-USD', 'MATIC-USD', stime='2022-05-01', ftime='2022-12-25').get_table())
    # print(Cr_Str1_0_0('BTC-USD', 'MATIC-USD', stime='2022-05-01').get_table())
    # print(Cr_Str1_0_0('BTC-USD', coin_new_popular, stime='2021-05-01').signals())
    # print(for_test(snp_more_b_09))