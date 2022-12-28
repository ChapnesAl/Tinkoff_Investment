import pandas as pd
from tokens import iss_token_full
from sql_investi.sql_str_tests import Db_str_tests
from result_mdl.play_ground_str1 import Str1_0_0, Str1_0_1
from result_mdl.play_ground_str3 import Str3_0_0, Str3_0_1, Str3_1_1
from result_mdl.play_ground_str4 import Str4_0_0, Str4_1_1, Str4_2_2






pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

mt = '^GSPC'  # '^GSPC', '^IXIC', '^RUT', '^DJI'
st = 'T'

btc = 'BTC-USD'
coin_list = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'XRP-USD', 'DOGE-USD', 'ADA-USD', 'MATIC-USD', 'WTRX-USD', 'DOT-USD', 'TRX-USD', 'LTC-USD', 'SHIB-USD', 'SOL-USD', 'HEX-USD', 'STETH-USD', 'UNI7083-USD', 'AVAX-USD', 'LEO-USD', 'LINK-USD', 'TON11419-USD']
coin_old_popular = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'XRP-USD', 'LINK-USD', 'DOGE-USD', 'ADA-USD', 'TRX-USD', 'LTC-USD']
coin_new_popular = ['MATIC-USD', 'WTRX-USD', 'DOT-USD', 'SHIB-USD', 'SOL-USD', 'HEX-USD', 'STETH-USD', 'UNI7083-USD', 'AVAX-USD', 'LEO-USD', 'TON11419-USD']



snp_b_15 = ['COTY', 'CCL', 'JWN', 'DXC', 'HAL', 'SLB', 'RCL', 'BFH', 'DVN', 'OXY', 'WYNN', 'PVH', 'GPS', 'XRX', 'BKR',
            'PARA', 'FCX', 'ALK', 'WDC', 'C', 'MOS', 'OKE', 'DHI', 'BBY', 'MPC', 'AMD', 'PRU', 'EXPE', 'EOG', 'VLO',
            'MAR', 'HCA', 'ALB']
snp_b_15_2 = ['GPS', 'XRX', 'BKR', 'PARA', 'FCX', 'ALK', 'WDC', 'C', 'MOS', 'OKE', 'DHI', 'BBY', 'MPC', 'AMD', 'PRU', 'EXPE', 'EOG', 'VLO', 'MAR', 'HCA', 'ALB']

snp_b_13_15 = ['KEY', 'WVB', 'BAC', 'LVS', 'UAL', 'HOG', 'CFG', 'ALK', 'MAS', 'BBY', 'EMR', 'PSX', 'MS', 'LYB', 'RTX', 'RL', 'COP', 'AMAT', 'QRVO', 'SPG', 'DRI', 'BA', 'META', 'NVDA', 'FDX', 'ADSK', 'ABMD', 'GS']

snp_b_09_11 = ['F', 'WU', 'KMI', 'CNP', 'HPQ', 'GLW', 'KHC', 'LUV', 'CMCSA', 'NRG', 'BK', 'CSCO', 'USB', 'TJX', 'CAH', 'HIG', 'SCHW', 'HAS', 'WELL', 'DXCM', 'ROST', 'GRMN', 'NKE', 'YUM', 'GOOGL', 'JPM', 'GOOG', 'GPN', 'MMM', 'AXP', 'TGT', 'TXN', 'CRM', 'NDAQ', 'CAT', 'ILMN', 'V', 'GD', 'NFLX', 'MSFT', 'HD', 'MA', 'SPGI', 'IDXX', 'ADBE', 'AVGO']

snp_b_11_13 = ['UAA', 'HBAN', 'HPE', 'IVZ', 'KEY', 'RF', 'BEN', 'WMB', 'DAL', 'GM', 'WRK', 'WFC', 'EBAY', 'VTR', 'AIG', 'MU', 'MET', 'NTAP', 'SYY', 'BXP', 'MNST', 'XOM', 'PYPL', 'DIS', 'TROW', 'HLT', 'QCOM', 'CVX', 'AAPL', 'HON', 'UPS', 'LOW', 'ACN', 'SNPS', 'LRCX', 'BKNG']

snp_more_b2 = ['COTY', 'CCL', 'JWN', 'DXC', 'HAL', 'SLB', 'RCL', 'BFH', 'DVN', 'OXY', 'WYNN', 'PVH']

more_stocks = ['EHTH', 'CCL', 'UAA', 'GPS', 'MAC', 'PUMP', 'ACH', 'ET', 'VIPS', 'PLTR', 'PTON', 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD',  'SHI', 'IVZ', 'M', 'WU', 'M', 'CNK', 'KMI', 'TRIP', 'LEVI', 'KEY', 'CHX', 'IBN', 'CHGG', 'RF', 'WB', 'JWN', 'LTHM', 'PINS', 'ANAB', 'T', 'UPWK', 'UBER', 'VREX', 'BJRI', 'BILI', 'SAVE', 'BEN', 'PARA', 'YY', 'FCX', 'BKR', 'RRC', 'TTM', 'HAL', 'CNP', 'SMAR', 'DXC', 'PPC', 'EVC', 'WMB', 'HPQ', 'DAL', 'USFD', 'BAC', 'APA', 'CLW', 'SLB', 'HOG', 'SPR', 'GM', 'PLAY', 'SAGE', 'BYND', 'LVS', 'Z', 'NRG', 'RCL', 'BSX', 'CFG', 'LI', 'WBA', 'KHC', 'EQT', 'CHEF', 'TWTR', 'INTC', 'TDOC', 'IRBT', 'WRK', 'UAL', 'LUV', 'BTI' , 'BFH', 'IRBT', 'BK', 'ALK', 'CMCSA', 'WFC', 'MO', 'ARWR', 'EQT', 'CSCO', 'VZ', 'KR', 'TTD', 'NEM', 'EBAY', 'AYX', 'IRM', 'PTR', 'NET', 'USB', 'CPRI', 'WDC', 'OVV', 'SNY', 'W', 'PFGC', 'MOS', 'TTE', 'AIG', 'C', 'VTR', 'DOW', 'MAS', 'BUD', 'NVAX', 'CAH', 'SIG', 'COIN', 'DVN', 'PVH', 'OKE', 'TJX', 'GILD', 'MET', 'REGI', 'MU', 'OXY', 'MDLZ', 'KO', 'JD', 'WYNN', 'EIX', 'DOCU', 'SCHW', 'HIG', 'CLR', 'OMC', 'NTAP', 'MTCH', 'BALL', 'BBY', 'SO', 'SQ', 'BMY', 'ORCL', 'HAS', 'STX', 'DHI', 'ROST', 'D', 'ADM', 'ATVI', 'INCY', 'FSLR', 'NEE', 'SBUX', 'MS', 'H', 'TWLO']

snp_more_b_09 = ['F', 'WU', 'KMI', 'CNP', 'HPQ', 'GLW', 'KHC', 'LUV', 'CMCSA', 'NRG', 'BK', 'CSCO', 'USB', 'TJX', 'CAH', 'HIG', 'SCHW', 'HAS', 'WELL', 'DXCM', 'ROST', 'GRMN', 'NKE', 'YUM', 'GOOGL', 'JPM', 'GOOG', 'GPN', 'MMM', 'AXP', 'TGT', 'TXN', 'CRM', 'NDAQ', 'CAT', 'ILMN', 'V', 'GD', 'NFLX', 'MSFT', 'HD', 'MA', 'SPGI', 'IDXX', 'ADBE', 'AVGO',
'UAA', 'HBAN', 'HPE', 'IVZ', 'KEY', 'RF', 'BEN', 'WMB', 'DAL', 'GM', 'WRK', 'WFC', 'EBAY', 'VTR', 'AIG', 'MU', 'MET', 'NTAP', 'SYY', 'BXP', 'MNST', 'XOM', 'PYPL', 'DIS', 'TROW', 'HLT', 'QCOM', 'CVX', 'AAPL', 'HON', 'UPS', 'LOW', 'ACN', 'SNPS', 'LRCX', 'BKNG',
'KEY', 'WVB', 'BAC', 'LVS', 'UAL', 'HOG', 'CFG', 'ALK', 'MAS', 'BBY', 'EMR', 'PSX', 'MS', 'LYB', 'RTX', 'RL', 'COP', 'AMAT', 'QRVO', 'SPG', 'DRI', 'BA', 'META', 'NVDA', 'FDX', 'ADSK', 'ABMD', 'GS',
'GPS', 'XRX', 'BKR', 'PARA', 'FCX', 'ALK', 'WDC', 'C', 'MOS', 'OKE', 'DHI', 'BBY', 'MPC', 'AMD', 'PRU', 'EXPE', 'EOG', 'VLO', 'MAR', 'HCA', 'ALB',
'COTY', 'CCL', 'JWN', 'DXC', 'HAL', 'SLB', 'RCL', 'BFH', 'DVN', 'OXY', 'WYNN', 'PVH']

snp_b_09_2 = ['F', 'WU', 'KMI', 'CNP', 'HPQ', 'GLW', 'KHC', 'LUV', 'CMCSA', 'NRG', 'BK', 'CSCO', 'USB', 'TJX', 'CAH', 'HIG', 'SCHW', 'HAS', 'WELL', 'DXCM', 'ROST', 'GRMN', 'NKE', 'YUM', 'GOOGL', 'JPM', 'GOOG', 'GPN', 'MMM', 'AXP', 'TGT', 'TXN', 'CRM', 'NDAQ', 'CAT', 'ILMN', 'V', 'GD', 'NFLX', 'MSFT', 'HD', 'MA', 'SPGI', 'IDXX', 'ADBE', 'AVGO',
'UAA', 'HBAN', 'HPE', 'IVZ', 'KEY', 'RF', 'BEN', 'WMB', 'DAL', 'GM', 'WRK', 'WFC', 'EBAY', 'VTR', 'AIG', 'MU', 'MET', 'NTAP', 'SYY', 'BXP', 'MNST', 'XOM', 'PYPL', 'DIS', 'TROW', 'HLT', 'QCOM', 'CVX', 'AAPL', 'HON', 'UPS', 'LOW', 'ACN', 'SNPS', 'LRCX', 'BKNG',
'KEY', 'WVB', 'BAC', 'LVS', 'UAL', 'HOG', 'CFG', 'ALK', 'MAS', 'BBY', 'EMR', 'PSX', 'MS', 'LYB', 'RTX', 'RL', 'COP', 'AMAT', 'QRVO', 'SPG', 'DRI', 'BA', 'META', 'NVDA', 'FDX', 'ADSK', 'ABMD', 'GS',
'GPS', 'XRX', 'BKR', 'PARA', 'FCX', 'ALK', 'WDC', 'C', 'MOS', 'OKE', 'DHI', 'BBY', 'MPC', 'AMD', 'PRU', 'EXPE', 'EOG', 'VLO', 'MAR', 'HCA', 'ALB']

# snb

""" Str 1 0 0"""




def for_test(slist, st_o):
    s1 = list(slist)
    s2 = list(slist)
    s3 = list(slist)
    s4 = list(slist)
    s5 = list(slist)
    s6 = list(slist)
    a = Str1_0_0('^GSPC', s1, stime='2018-05-01', ftime='2020-01-01', interval='1d', str_opt=st_o).sum_results()
    b = Str1_0_0('^GSPC', s2, stime='2019-05-01', ftime='2020-06-01', interval='1d', str_opt=st_o).sum_results()
    c = Str1_0_0('^GSPC', s3, stime='2019-10-01', ftime='2021-01-01', interval='1d', str_opt=st_o).sum_results()
    d = Str1_0_0('^GSPC', s4, stime='2020-05-01', ftime='2021-10-01', interval='1d', str_opt=st_o).sum_results()
    e = Str1_0_0('^GSPC', s5, stime='2021-06-01', ftime='2022-04-03', interval='1d', str_opt=st_o).sum_results()
    f = Str1_0_0('^GSPC', s6, stime='2022-01-01', interval='1d', str_opt=st_o).sum_results()

    return a, b, c, d, e, f, st_o


def pack_analyse(slist, pack_st_op):
    l = list(pack_st_op)
    for i in range(len(pack_st_op)):
        l[i] = for_test(slist, pack_st_op[i])
    return tuple(l)


""" Import Strategy Option"""
from strategies.str_options_4column import p1_mr, p2_mr, p3_mr, p4_mr, p5_mr, p6_mr, p7_mr, p8_mr, p9_mr, p10_mr,\
    p1_lr, p2_lr, p3_lr, p4_lr, p5_lr, p6_lr, p7_lr, p8_lr, p9_lr,\
    p1_plus1, p2_plus1, p3_plus1, p4_plus1, p5_plus1, p6_plus1, p7_plus1, p8_plus1
    # p1_cr_plus1


# Db_str_tests().insert_line_data(for_test(snp_b_15, mrAM_MmrB15_a_mrAM1_a_mrBL05))
Db_str_tests().insert_pack_data(pack_analyse(snp_b_15, p3_lr))
# Db_str_tests().del_all()
# Db_str_tests().create_table()
# Db_str_tests().get_full_table()


# Str1_0_0('^GSPC', snp_b_09_2, stime='2022-06-01', interval='1wk', str_opt="gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] + 1, 2] - 0)").signals()