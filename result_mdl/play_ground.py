from get_tables.table_str3 import ts3
from get_tables.table_str3_rus import ts3_rus
from result_mdl.base_rsl import Base_mdl
from paper_filter.lists_papers import val_all_usd, val_long_usd, val_long_rub, val_all_rub
import pandas as pd


market_tick = '^GSPC'
# market_tick = '^IXIC'
# market_tick = '^RUT'
# market_tick = '^DJI'

share_tick = 'T'
# share_tick = ['AAL', 'ACN', 'AMD']
# share_tick = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB']
# share_tick = ['EAR', 'ZYNE', 'ASTR', 'BYSI', 'CORR', 'CRTX', 'CLOV', 'WKHS', 'HRTX', 'MFGP']
# share_tick = ['PBI', 'RKLB', 'CLSK', 'MOMO', 'RIOT', 'MLCO', 'LPL', 'SWN', 'GTHX', 'ETRN']
# share_tick = ['SPCE', 'GOSS', 'COTY', 'ZYXI', 'LFC', 'RRGB', 'ATRA', 'MARA',  'AERI', 'EHTH']
# share_tick = ['CCL', 'UAA', 'GPS', 'MAC', 'PUMP', 'ACH', 'ET', 'VIPS', 'PLTR', 'PTON']
# share_tick = ['PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT']

# share_tick =['ABBV', 'AA', 'VEON', 'EAR', 'ASTR', 'BYSI', 'CORR', 'CRTX', 'CLOV', 'WKHS', 'MFGP', 'RKLB',
#              'CLSK', 'RIOT', 'SWN', 'GTHX', 'SPCE', 'COTY', 'MARA', 'EHTH', 'ACH', 'VIPS', 'PCG', 'PAGS', 'GT', 'IOVA', 'TWOU', 'LYFT']

# share_tick = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'EAR', 'ZYNE', 'ASTR', 'BYSI', 'CORR', 'CRTX', 'CLOV', 'WKHS', 'HRTX', 'MFGP'
#         , 'PBI', 'RKLB', 'CLSK', 'MOMO', 'RIOT', 'MLCO', 'LPL', 'SWN', 'GTHX', 'ETRN', 'SPCE', 'GOSS', 'COTY', 'ZYXI', 'LFC', 'RRGB', 'ATRA', 'MARA',  'AERI', 'EHTH', 'CCL', 'UAA', 'GPS', 'MAC', 'PUMP', 'ACH', 'ET', 'VIPS', 'PLTR', 'PTON'
#         , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT']

# share_tick = ["HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD', 'SHI', 'IVZ', 'M', 'WU', 'M', 'CNK', 'KMI', 'TRIP', 'LEVI', 'KEY', 'CHX', 'IBN', 'CHGG', 'RF', 'WB', 'JWN', 'LTHM', 'PINS', 'ANAB', 'T', 'UPWK', 'UBER', 'VREX', 'BJRI', 'BILI', 'SAVE', 'BEN', 'PARA', 'YY', 'FCX', 'BKR', 'RRC']

# 2,3,4,6,8,9
# share_tick = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'EAR', 'ZYNE', 'ASTR', 'BYSI', 'CORR', 'CRTX', 'CLOV', 'WKHS', 'HRTX', 'MFGP'
#         , 'PBI', 'RKLB', 'CLSK', 'MOMO', 'RIOT', 'MLCO', 'LPL', 'SWN', 'GTHX', 'ETRN', 'SPCE', 'GOSS', 'COTY', 'ZYXI', 'LFC', 'RRGB', 'ATRA', 'MARA',  'AERI', 'EHTH', 'CCL', 'UAA', 'GPS', 'MAC', 'PUMP', 'ACH', 'ET', 'VIPS', 'PLTR', 'PTON'
#         , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
#          ,  'SHI', 'IVZ', 'M', 'WU', 'M', 'CNK', 'KMI', 'TRIP', 'LEVI', 'KEY', 'CHX', 'IBN', 'CHGG', 'RF', 'WB', 'JWN', 'LTHM', 'PINS', 'ANAB', 'T', 'UPWK', 'UBER', 'VREX', 'BJRI', 'BILI', 'SAVE', 'BEN', 'PARA', 'YY', 'FCX', 'BKR', 'RRC'
#        , 'TTM', 'HAL', 'CNP', 'SMAR', 'DXC', 'PPC', 'EVC', 'WMB', 'HPQ', 'DAL', 'USFD', 'BAC', 'APA', 'CLW', 'SLB', 'HOG', 'SPR', 'GM', 'PLAY', 'SAGE', 'BYND', 'LVS', 'Z', 'NRG', 'RCL', 'BSX', 'CFG', 'LI', 'WBA', 'KHC', 'EQT', 'CHEF', 'TWTR', 'INTC', 'TDOC', 'IRBT', 'WRK', 'UAL', 'LUV'
#               , 'BTI' , 'BFH', 'IRBT', 'BK', 'ALK', 'CMCSA', 'WFC', 'MO', 'ARWR', 'EQT', 'CSCO', 'VZ', 'KR', 'TTD', 'NEM', 'EBAY', 'AYX', 'IRM', 'PTR', 'NET', 'USB', 'CPRI', 'WDC', 'OVV', 'SNY', 'W', 'PFGC', 'MOS', 'TTE', 'AIG', 'C', 'VTR', 'DOW', 'MAS', 'BUD', 'NVAX', 'CAH', 'SIG', 'COIN', 'DVN', 'PVH'
#             , 'OKE', 'TJX', 'GILD', 'MET', 'REGI', 'MU', 'OXY', 'MDLZ', 'KO', 'JD', 'WYNN', 'EIX', 'DOCU', 'SCHW', 'HIG', 'CLR', 'OMC', 'NTAP', 'MTCH', 'BALL', 'BBY', 'SO', 'SQ', 'BMY', 'ORCL', 'HAS', 'STX', 'DHI', 'ROST', 'D', 'ADM', 'ATVI', 'INCY', 'FSLR', 'NEE', 'SBUX', 'MS', 'H', 'TWLO']

""" val_all_usd val_long_rub val_long_usd """
# share_tick = val_all_usd
# val_all_usd, val_long_usd, val_long_rub, val_all_rub




'''Strategy 1'''
# if type(share_tick) == str:
#     print(rt1(ts1(market_tick,share_tick)))
# else:
#     for i in range(len(share_tick)):
#         share_tick[i] = rt1(ts1(market_tick, share_tick[i]))
#     print(share_tick)
#     print(sum(share_tick))


'''Strategy 2 - Numbers'''
# if type(share_tick) == str:
#     print(Base_mdl(ts2(market_tick, share_tick)).rt2())
#     # print(rt2(ts2(market_tick, share_tick)))
#     # print(ts2(market_tick,share_tick))
# else:
#     for i in range(len(share_tick)):
#         share_tick[i] =(Base_mdl(ts2(market_tick, share_tick[i])).rt2())
#         # share_tick[i] = rt2(ts2(market_tick, share_tick[i]))
#     print(share_tick)
#     print(sum(share_tick))


'''Strategy 2 - Signals'''
""" !!! ADD LAST MONTH (NOW 6) !!! """

# if type(share_tick) == str or None:
#     print(Base_mdl(ts2(market_tick, share_tick)).signal2())
# else:
#     copy_names = share_tick.copy()
#     for i in range(len(share_tick)):
#         share_tick[i] = Base_mdl(ts2(market_tick, share_tick[i])).signal2()
#         # share_tick[i] = signal2(ts2(market_tick, share_tick[i])) # command before class update
#     d = {"Companies": copy_names, 'Signals': share_tick}
#     df = pd.DataFrame(data=d)
#     print(df[(df.Signals == 'Buy') | (df.Signals == 'Sell')])


'''Strategy 2 - Day High and Low'''
''' Only 1 ticker'''
# print(ts2_minutes(share_tick))


'''Strategy 2 - Get table'''
''' Only 1 ticker'''
# print(ts2(market_tick, share_tick))


'''Strategy 2 - Get Result of Month to Month'''
''' Only 1 ticker'''
# Base_mdl(ts2(market_tick, share_tick)).date_sum2()



# '''Strategy 3 - Numbers Sum Results'''
# if type(share_tick) == str:
#     print(Base_mdl(ts3(market_tick, share_tick)).rt2())
#     # print(rt2(ts2(market_tick, share_tick)))
#     # print(ts2(market_tick,share_tick))
# else:
#     for i in range(len(share_tick)):
#         try:
#             share_tick[i] =(Base_mdl(ts3(market_tick, share_tick[i])).rt2())
#             # share_tick[i] = rt2(ts2(market_tick, share_tick[i]))
#         except:
#             share_tick[i] = 0
#     print(share_tick)
#     print(sum(share_tick))


'''Strategy 3 - Numbers Sum Results RUS MARKET'''
# if len(share_tick) == 2:
#     print(Base_mdl(ts3_rus(*share_tick)).rt2())
#     # print(rt2(ts2(market_tick, share_tick)))
#     # print(ts2(market_tick,share_tick))
# else:
#     for i in range(len(share_tick)):
#         x = share_tick[i]
#         try:
#             share_tick[i] =(Base_mdl(ts3_rus(*x)).rt2())
#             # share_tick[i] = rt2(ts2(market_tick, share_tick[i]))
#         except:
#             share_tick[i] = 0
#     print(share_tick)
#     print(sum(share_tick))




'''Strategy 3 - Signals'''
'''   !!!  Add short period  !!!  '''
""" !!! ADD LAST MONTH (NOW JUNE 6) !!! """
# if type(share_tick) == str or None:
#     print(Base_mdl(ts3(market_tick, share_tick)).signal2())
# else:
#     copy_names = share_tick.copy()
#     for i in range(len(share_tick)):
#         try:
#             share_tick[i] = (Base_mdl(ts3(market_tick, share_tick[i])).signal2())
#             # share_tick[i] = signal2(ts2(market_tick, share_tick[i])) # command before class update
#             d = {"Companies": copy_names, 'Signals': share_tick}
#         except:
#             share_tick[i] = 0
#     df = pd.DataFrame(data=d)
#     print(df[(df.Signals == 'Buy') | (df.Signals == 'Sell') | (df.Signals == 'Buy') | (df.Signals == 'Sell')])



'''Strategy 3 - Day High and Low'''
''' Only 1 ticker'''
# print(ts2_minutes(share_tick))


'''Strategy 3 - Get table'''
''' Only 1 ticker'''
# print(ts3(market_tick, share_tick))


'''Strategy 3 - Get Result of Month to Month'''
''' Only 1 ticker'''
# pprint(Base_mdl(ts3(market_tick, share_tick)).date_sum2())


'''Strategy 3 - Get Results of Month to Month Without any months'''
''' WITH LAST CURRENT MONTH (6 now)'''
#
if type(share_tick) == str:
    print(Base_mdl(ts3(market_tick, share_tick)).del_any_months())
else:
    for i in range(len(share_tick)):
        share_tick[i] =(Base_mdl(ts3(market_tick, share_tick[i])).del_any_months())
    print(share_tick)
    print(sum(share_tick))
