from result_mdl.play_ground_str3 import Str3_0_0, Str3_0_1, Str3_1_1
from result_mdl.play_ground_str4 import Str4_0_0
from paper_filter.lists_papers import val_all_usd, val_long_usd, val_long_rub, val_all_rub

mt = '^GSPC' # '^GSPC', '^IXIC', '^RUT', '^DJI'
st = 'T'
share_tick = ["HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD', 'SHI', 'IVZ', 'M', 'WU', 'M', 'CNK', 'KMI', 'TRIP', 'LEVI', 'KEY', 'CHX', 'IBN', 'CHGG', 'RF', 'WB', 'JWN', 'LTHM', 'PINS', 'ANAB', 'T', 'UPWK', 'UBER', 'VREX', 'BJRI', 'BILI', 'SAVE', 'BEN', 'PARA', 'YY', 'FCX', 'BKR', 'RRC']
share_tick1 = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'EAR', 'ZYNE', 'ASTR', 'BYSI', 'CORR', 'CRTX', 'CLOV', 'WKHS', 'HRTX', 'MFGP'
        , 'PBI', 'RKLB', 'CLSK', 'MOMO', 'RIOT', 'MLCO', 'LPL', 'SWN', 'GTHX', 'ETRN', 'SPCE', 'GOSS', 'COTY', 'ZYXI', 'LFC', 'RRGB', 'ATRA', 'MARA',  'AERI', 'EHTH', 'CCL', 'UAA', 'GPS', 'MAC', 'PUMP', 'ACH', 'ET', 'VIPS', 'PLTR', 'PTON'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
         ,  'SHI', 'IVZ', 'M', 'WU', 'M', 'CNK', 'KMI', 'TRIP', 'LEVI', 'KEY', 'CHX', 'IBN', 'CHGG', 'RF', 'WB', 'JWN', 'LTHM', 'PINS', 'ANAB', 'T', 'UPWK', 'UBER', 'VREX', 'BJRI', 'BILI', 'SAVE', 'BEN', 'PARA', 'YY', 'FCX', 'BKR', 'RRC'
       , 'TTM', 'HAL', 'CNP', 'SMAR', 'DXC', 'PPC', 'EVC', 'WMB', 'HPQ', 'DAL', 'USFD', 'BAC', 'APA', 'CLW', 'SLB', 'HOG', 'SPR', 'GM', 'PLAY', 'SAGE', 'BYND', 'LVS', 'Z', 'NRG', 'RCL', 'BSX', 'CFG', 'LI', 'WBA', 'KHC', 'EQT', 'CHEF', 'TWTR', 'INTC', 'TDOC', 'IRBT', 'WRK', 'UAL', 'LUV'
              , 'BTI' , 'BFH', 'IRBT', 'BK', 'ALK', 'CMCSA', 'WFC', 'MO', 'ARWR', 'EQT', 'CSCO', 'VZ', 'KR', 'TTD', 'NEM', 'EBAY', 'AYX', 'IRM', 'PTR', 'NET', 'USB', 'CPRI', 'WDC', 'OVV', 'SNY', 'W', 'PFGC', 'MOS', 'TTE', 'AIG', 'C', 'VTR', 'DOW', 'MAS', 'BUD', 'NVAX', 'CAH', 'SIG', 'COIN', 'DVN', 'PVH'
            , 'OKE', 'TJX', 'GILD', 'MET', 'REGI', 'MU', 'OXY', 'MDLZ', 'KO', 'JD', 'WYNN', 'EIX', 'DOCU', 'SCHW', 'HIG', 'CLR', 'OMC', 'NTAP', 'MTCH', 'BALL', 'BBY', 'SO', 'SQ', 'BMY', 'ORCL', 'HAS', 'STX', 'DHI', 'ROST', 'D', 'ADM', 'ATVI', 'INCY', 'FSLR', 'NEE', 'SBUX', 'MS', 'H', 'TWLO']


"""  3 0 0 """

# print(Str3_0_0('^GSPC', 'T').signals())
# print(Str3_0_0(mt, 'T').sum_results())
# print(Str3_0_0('^GSPC', 'T').get_table())
# print(Str3_0_0('^GSPC', 'T').month_results())
# print(Str3_0_0('^GSPC', ['T', 'AA']).month_results_without_bad())
# print(Str3_0_0('^GSPC', val_all_rub).sum_results_rus())
# print(Str3_0_0(mt, val_long_usd).sum_results())


"""  3 0 1 """

# print(Str3_0_1(mt, val_all_usd).sum_results())


"""  3 1 1 """

# print(Str3_1_1(mt, share_tick1).sum_results())
# print(Str3_1_1(mt, val_all_usd).sum_results())
print(Str3_1_1('^GSPC', 'HEAR').get_table())
print(Str3_1_1('^GSPC', 'HEAR', interval='1wk').get_table())


"""  4 0 0 """

# print(Str4_0_0('^GSPC', 'T').get_table())
# print(Str4_0_0(mt, share_tick).sum_results())
# print(Str4_0_0(mt, val_all_usd).sum_results())