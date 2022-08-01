
from get_tables.table_str3 import ts4
from result_mdl.base_rsl import Base_mdl

market_tick = '^GSPC'
# market_tick = '^IXIC'
# market_tick = '^RUT'
# market_tick = '^DJI'

# share_tick = 'acn'
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
share_tick = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'EAR', 'ZYNE', 'ASTR', 'BYSI', 'CORR', 'CRTX', 'CLOV', 'WKHS', 'HRTX', 'MFGP'
        , 'PBI', 'RKLB', 'CLSK', 'MOMO', 'RIOT', 'MLCO', 'LPL', 'SWN', 'GTHX', 'ETRN', 'SPCE', 'GOSS', 'COTY', 'ZYXI', 'LFC', 'RRGB', 'ATRA', 'MARA',  'AERI', 'EHTH', 'CCL', 'UAA', 'GPS', 'MAC', 'PUMP', 'ACH', 'ET', 'VIPS', 'PLTR', 'PTON'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
         ,  'SHI', 'IVZ', 'M', 'WU', 'M', 'CNK', 'KMI', 'TRIP', 'LEVI', 'KEY', 'CHX', 'IBN', 'CHGG', 'RF', 'WB', 'JWN', 'LTHM', 'PINS', 'ANAB', 'T', 'UPWK', 'UBER', 'VREX', 'BJRI', 'BILI', 'SAVE', 'BEN', 'PARA', 'YY', 'FCX', 'BKR', 'RRC'
       , 'TTM', 'HAL', 'CNP', 'SMAR', 'DXC', 'PPC', 'EVC', 'WMB', 'HPQ', 'DAL', 'USFD', 'BAC', 'APA', 'CLW', 'SLB', 'HOG', 'SPR', 'GM', 'PLAY', 'SAGE', 'BYND', 'LVS', 'Z', 'NRG', 'RCL', 'BSX', 'CFG', 'LI', 'WBA', 'KHC', 'EQT', 'CHEF', 'TWTR', 'INTC', 'TDOC', 'IRBT', 'WRK', 'UAL', 'LUV']




'''Strategy 4 - Numbers Sum Results'''
if type(share_tick) == str:
    print(Base_mdl(ts4(market_tick, share_tick)).rt2())
else:
    for i in range(len(share_tick)):
        try:
            share_tick[i] =(Base_mdl(ts4(market_tick, share_tick[i])).rt2())
        except:
            share_tick[i] = 0
    print(share_tick)
    print(sum(share_tick))


