
from result_mdl.play_ground_str3 import Str3_0_0, Str3_0_1, Str3_1_1
from result_mdl.play_ground_str4 import Str4_0_0, Str4_1_1, Str4_2_2
from paper_filter.lists_papers import val_all_usd, val_long_usd, val_long_rub, val_all_rub

from tickers import p_a, p_b, p_c, p_d, p_e, p_f
from tickers import p2_a, p2_b, p2_c, p2_d, p2_e, p2_f
from tickers import snp_b2, snp_b2a, snp_b2b, snp_b2c, snp_b2d, snp_b2e
from tickers import snp_b_15_2, snp_b_15_2a, snp_b_15_2b, snp_b_15_2c, snp_b_15_2d, snp_b_15_2e
from tickers import snp_b_13_15, snp_b_13_15a, snp_b_13_15b,  snp_b_13_15c, snp_b_13_15d, snp_b_13_15e
from tickers import snp_b_11_13,  snp_b_11_13a,  snp_b_11_13b, snp_b_11_13c, snp_b_11_13d, snp_b_11_13e
from tickers import snp_b_09_11, snp_b_09_11a, snp_b_09_11b, snp_b_09_11c, snp_b_09_11d, snp_b_09_11e
from tickers import b_15_plus, b_15_plus_a, b_15_plus_b, b_15_plus_c, b_15_plus_d, b_15_plus_e
from tickers import snp_b_15, snp_b_15a, snp_b_15b, snp_b_15c, snp_b_15d, snp_b_15e


mt = '^GSPC' # '^GSPC', '^IXIC', '^RUT', '^DJI'
st = 'T'
# share_tick = ["HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD', 'SHI', 'IVZ', 'M', 'WU', 'M', 'CNK', 'KMI', 'TRIP', 'LEVI', 'KEY', 'CHX', 'IBN', 'CHGG', 'RF', 'WB', 'JWN', 'LTHM', 'PINS', 'ANAB', 'T', 'UPWK', 'UBER', 'VREX', 'BJRI', 'BILI', 'SAVE', 'BEN', 'PARA', 'YY', 'FCX', 'BKR', 'RRC']
# share_tick1 = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'EAR', 'ZYNE', 'ASTR', 'BYSI', 'CORR', 'CRTX', 'CLOV', 'WKHS', 'HRTX', 'MFGP'
#         , 'PBI', 'RKLB', 'CLSK', 'MOMO', 'RIOT', 'MLCO', 'LPL', 'SWN', 'GTHX', 'ETRN', 'SPCE', 'GOSS', 'COTY', 'ZYXI', 'LFC', 'RRGB', 'ATRA', 'MARA',  'AERI', 'EHTH', 'CCL', 'UAA', 'GPS', 'MAC', 'PUMP', 'ACH', 'ET', 'VIPS', 'PLTR', 'PTON'
#         , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
#          ,  'SHI', 'IVZ', 'M', 'WU', 'M', 'CNK', 'KMI', 'TRIP', 'LEVI', 'KEY', 'CHX', 'IBN', 'CHGG', 'RF', 'WB', 'JWN', 'LTHM', 'PINS', 'ANAB', 'T', 'UPWK', 'UBER', 'VREX', 'BJRI', 'BILI', 'SAVE', 'BEN', 'PARA', 'YY', 'FCX', 'BKR', 'RRC'
#        , 'TTM']

share_tick1 = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM']

share_tick11 = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM']


share_tick1a = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM']

share_tick1aa = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM']

share_tick1b = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM']

share_tick1bb = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM']

share_tick1c = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM']

share_tick1cc = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM']

share_tick1d = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM']

share_tick1dd = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM']

share_tick1e = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM']

share_tick1ee = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM']


sec_share_tick1c = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM', 'HAL', 'CNP', 'SMAR', 'DXC', 'PPC', 'EVC', 'WMB', 'HPQ', 'DAL', 'USFD', 'BAC', 'APA', 'CLW', 'SLB', 'HOG', 'SPR', 'GM', 'PLAY', 'SAGE', 'BYND', 'LVS', 'Z', 'NRG', 'RCL', 'BSX', 'CFG', 'LI', 'WBA', 'KHC', 'EQT', 'CHEF', 'TWTR', 'INTC', 'TDOC', 'IRBT', 'WRK', 'UAL', 'LUV'
               , 'BTI' , 'BFH', 'IRBT', 'BK', 'ALK', 'CMCSA', 'WFC', 'MO', 'ARWR', 'EQT', 'CSCO', 'VZ', 'KR', 'TTD', 'NEM', 'EBAY', 'AYX', 'IRM', 'PTR', 'NET', 'USB', 'CPRI', 'WDC', 'OVV', 'SNY', 'W', 'PFGC', 'MOS', 'TTE', 'AIG', 'C', 'VTR', 'DOW', 'MAS', 'BUD', 'NVAX', 'CAH', 'SIG', 'COIN', 'DVN', 'PVH'
           , 'OKE', 'TJX', 'GILD', 'MET', 'REGI', 'MU', 'OXY', 'MDLZ', 'KO', 'JD', 'WYNN', 'EIX', 'DOCU', 'SCHW', 'HIG', 'CLR', 'OMC', 'NTAP', 'MTCH', 'BALL', 'BBY', 'SO', 'SQ', 'BMY', 'ORCL', 'HAS', 'STX', 'DHI', 'ROST', 'D', 'ADM', 'ATVI', 'INCY', 'FSLR', 'NEE', 'SBUX', 'MS', 'H', 'TWLO']



sec_share_tick1cc = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM', 'HAL', 'CNP', 'SMAR', 'DXC', 'PPC', 'EVC', 'WMB', 'HPQ', 'DAL', 'USFD', 'BAC', 'APA', 'CLW', 'SLB', 'HOG', 'SPR', 'GM', 'PLAY', 'SAGE', 'BYND', 'LVS', 'Z', 'NRG', 'RCL', 'BSX', 'CFG', 'LI', 'WBA', 'KHC', 'EQT', 'CHEF', 'TWTR', 'INTC', 'TDOC', 'IRBT', 'WRK', 'UAL', 'LUV'
               , 'BTI' , 'BFH', 'IRBT', 'BK', 'ALK', 'CMCSA', 'WFC', 'MO', 'ARWR', 'EQT', 'CSCO', 'VZ', 'KR', 'TTD', 'NEM', 'EBAY', 'AYX', 'IRM', 'PTR', 'NET', 'USB', 'CPRI', 'WDC', 'OVV', 'SNY', 'W', 'PFGC', 'MOS', 'TTE', 'AIG', 'C', 'VTR', 'DOW', 'MAS', 'BUD', 'NVAX', 'CAH', 'SIG', 'COIN', 'DVN', 'PVH'
           , 'OKE', 'TJX', 'GILD', 'MET', 'REGI', 'MU', 'OXY', 'MDLZ', 'KO', 'JD', 'WYNN', 'EIX', 'DOCU', 'SCHW', 'HIG', 'CLR', 'OMC', 'NTAP', 'MTCH', 'BALL', 'BBY', 'SO', 'SQ', 'BMY', 'ORCL', 'HAS', 'STX', 'DHI', 'ROST', 'D', 'ADM', 'ATVI', 'INCY', 'FSLR', 'NEE', 'SBUX', 'MS', 'H', 'TWLO']


sec_share_tick1d = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM', 'HAL', 'CNP', 'SMAR', 'DXC', 'PPC', 'EVC', 'WMB', 'HPQ', 'DAL', 'USFD', 'BAC', 'APA', 'CLW', 'SLB', 'HOG', 'SPR', 'GM', 'PLAY', 'SAGE', 'BYND', 'LVS', 'Z', 'NRG', 'RCL', 'BSX', 'CFG', 'LI', 'WBA', 'KHC', 'EQT', 'CHEF', 'TWTR', 'INTC', 'TDOC', 'IRBT', 'WRK', 'UAL', 'LUV'
               , 'BTI' , 'BFH', 'IRBT', 'BK', 'ALK', 'CMCSA', 'WFC', 'MO', 'ARWR', 'EQT', 'CSCO', 'VZ', 'KR', 'TTD', 'NEM', 'EBAY', 'AYX', 'IRM', 'PTR', 'NET', 'USB', 'CPRI', 'WDC', 'OVV', 'SNY', 'W', 'PFGC', 'MOS', 'TTE', 'AIG', 'C', 'VTR', 'DOW', 'MAS', 'BUD', 'NVAX', 'CAH', 'SIG', 'COIN', 'DVN', 'PVH'
           , 'OKE', 'TJX', 'GILD', 'MET', 'REGI', 'MU', 'OXY', 'MDLZ', 'KO', 'JD', 'WYNN', 'EIX', 'DOCU', 'SCHW', 'HIG', 'CLR', 'OMC', 'NTAP', 'MTCH', 'BALL', 'BBY', 'SO', 'SQ', 'BMY', 'ORCL', 'HAS', 'STX', 'DHI', 'ROST', 'D', 'ADM', 'ATVI', 'INCY', 'FSLR', 'NEE', 'SBUX', 'MS', 'H', 'TWLO']


sec_share_tick1dd = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM', 'HAL', 'CNP', 'SMAR', 'DXC', 'PPC', 'EVC', 'WMB', 'HPQ', 'DAL', 'USFD', 'BAC', 'APA', 'CLW', 'SLB', 'HOG', 'SPR', 'GM', 'PLAY', 'SAGE', 'BYND', 'LVS', 'Z', 'NRG', 'RCL', 'BSX', 'CFG', 'LI', 'WBA', 'KHC', 'EQT', 'CHEF', 'TWTR', 'INTC', 'TDOC', 'IRBT', 'WRK', 'UAL', 'LUV'
               , 'BTI' , 'BFH', 'IRBT', 'BK', 'ALK', 'CMCSA', 'WFC', 'MO', 'ARWR', 'EQT', 'CSCO', 'VZ', 'KR', 'TTD', 'NEM', 'EBAY', 'AYX', 'IRM', 'PTR', 'NET', 'USB', 'CPRI', 'WDC', 'OVV', 'SNY', 'W', 'PFGC', 'MOS', 'TTE', 'AIG', 'C', 'VTR', 'DOW', 'MAS', 'BUD', 'NVAX', 'CAH', 'SIG', 'COIN', 'DVN', 'PVH'
           , 'OKE', 'TJX', 'GILD', 'MET', 'REGI', 'MU', 'OXY', 'MDLZ', 'KO', 'JD', 'WYNN', 'EIX', 'DOCU', 'SCHW', 'HIG', 'CLR', 'OMC', 'NTAP', 'MTCH', 'BALL', 'BBY', 'SO', 'SQ', 'BMY', 'ORCL', 'HAS', 'STX', 'DHI', 'ROST', 'D', 'ADM', 'ATVI', 'INCY', 'FSLR', 'NEE', 'SBUX', 'MS', 'H', 'TWLO']

sec_share_tick1e = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM', 'HAL', 'CNP', 'SMAR', 'DXC', 'PPC', 'EVC', 'WMB', 'HPQ', 'DAL', 'USFD', 'BAC', 'APA', 'CLW', 'SLB', 'HOG', 'SPR', 'GM', 'PLAY', 'SAGE', 'BYND', 'LVS', 'Z', 'NRG', 'RCL', 'BSX', 'CFG', 'LI', 'WBA', 'KHC', 'EQT', 'CHEF', 'TWTR', 'INTC', 'TDOC', 'IRBT', 'WRK', 'UAL', 'LUV'
               , 'BTI' , 'BFH', 'IRBT', 'BK', 'ALK', 'CMCSA', 'WFC', 'MO', 'ARWR', 'EQT', 'CSCO', 'VZ', 'KR', 'TTD', 'NEM', 'EBAY', 'AYX', 'IRM', 'PTR', 'NET', 'USB', 'CPRI', 'WDC', 'OVV', 'SNY', 'W', 'PFGC', 'MOS', 'TTE', 'AIG', 'C', 'VTR', 'DOW', 'MAS', 'BUD', 'NVAX', 'CAH', 'SIG', 'COIN', 'DVN', 'PVH'
           , 'OKE', 'TJX', 'GILD', 'MET', 'REGI', 'MU', 'OXY', 'MDLZ', 'KO', 'JD', 'WYNN', 'EIX', 'DOCU', 'SCHW', 'HIG', 'CLR', 'OMC', 'NTAP', 'MTCH', 'BALL', 'BBY', 'SO', 'SQ', 'BMY', 'ORCL', 'HAS', 'STX', 'DHI', 'ROST', 'D', 'ADM', 'ATVI', 'INCY', 'FSLR', 'NEE', 'SBUX', 'MS', 'H', 'TWLO']

sec_share_tick1ee = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'KR', 'ZYNE', 'M', 'BYSI', 'CORR', 'CRTX', 'EBAY', 'WKHS', 'HRTX', 'MFGP'
        , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
       , 'TTM', 'HAL', 'CNP', 'SMAR', 'DXC', 'PPC', 'EVC', 'WMB', 'HPQ', 'DAL', 'USFD', 'BAC', 'APA', 'CLW', 'SLB', 'HOG', 'SPR', 'GM', 'PLAY', 'SAGE', 'BYND', 'LVS', 'Z', 'NRG', 'RCL', 'BSX', 'CFG', 'LI', 'WBA', 'KHC', 'EQT', 'CHEF', 'TWTR', 'INTC', 'TDOC', 'IRBT', 'WRK', 'UAL', 'LUV'
               , 'BTI' , 'BFH', 'IRBT', 'BK', 'ALK', 'CMCSA', 'WFC', 'MO', 'ARWR', 'EQT', 'CSCO', 'VZ', 'KR', 'TTD', 'NEM', 'EBAY', 'AYX', 'IRM', 'PTR', 'NET', 'USB', 'CPRI', 'WDC', 'OVV', 'SNY', 'W', 'PFGC', 'MOS', 'TTE', 'AIG', 'C', 'VTR', 'DOW', 'MAS', 'BUD', 'NVAX', 'CAH', 'SIG', 'COIN', 'DVN', 'PVH'
           , 'OKE', 'TJX', 'GILD', 'MET', 'REGI', 'MU', 'OXY', 'MDLZ', 'KO', 'JD', 'WYNN', 'EIX', 'DOCU', 'SCHW', 'HIG', 'CLR', 'OMC', 'NTAP', 'MTCH', 'BALL', 'BBY', 'SO', 'SQ', 'BMY', 'ORCL', 'HAS', 'STX', 'DHI', 'ROST', 'D', 'ADM', 'ATVI', 'INCY', 'FSLR', 'NEE', 'SBUX', 'MS', 'H', 'TWLO']




# share_tick2 = ['AAL', 'ACN', 'AMD', 'ABBV', 'AA', 'APLE', 'NFLX', 'VEON', 'SLDB', 'EAR', 'ZYNE', 'ASTR', 'BYSI', 'CORR', 'CRTX', 'CLOV', 'WKHS', 'HRTX', 'MFGP'
#         , 'PBI', 'RKLB', 'CLSK', 'MOMO', 'RIOT', 'MLCO', 'LPL', 'SWN', 'GTHX', 'ETRN', 'SPCE', 'GOSS', 'COTY', 'ZYXI', 'LFC', 'RRGB', 'ATRA', 'MARA',  'AERI', 'EHTH', 'CCL', 'UAA', 'GPS', 'MAC', 'PUMP', 'ACH', 'ET', 'VIPS', 'PLTR', 'PTON'
#         , 'PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT', "HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD'
#          ,  'SHI', 'IVZ', 'M', 'WU', 'CNK', 'KMI', 'TRIP', 'LEVI', 'KEY', 'CHX', 'IBN', 'CHGG', 'RF', 'WB', 'JWN', 'LTHM', 'PINS', 'ANAB', 'T', 'UPWK', 'UBER', 'VREX', 'BJRI', 'BILI', 'SAVE', 'BEN', 'PARA', 'YY', 'FCX', 'BKR', 'RRC'
#        , 'TTM', 'HAL', 'CNP', 'SMAR', 'DXC', 'PPC', 'EVC', 'WMB', 'HPQ', 'DAL', 'USFD', 'BAC', 'APA', 'CLW', 'SLB', 'HOG', 'SPR', 'GM', 'PLAY', 'SAGE', 'BYND', 'LVS', 'Z', 'NRG', 'RCL', 'BSX', 'CFG', 'LI', 'WBA', 'KHC', 'EQT', 'CHEF', 'TWTR', 'INTC', 'TDOC', 'IRBT', 'WRK', 'UAL', 'LUV'
#               , 'BTI' , 'BFH', 'IRBT', 'BK', 'ALK', 'CMCSA', 'WFC', 'MO', 'ARWR', 'EQT', 'CSCO', 'VZ', 'KR', 'TTD', 'NEM', 'EBAY', 'AYX', 'IRM', 'PTR', 'NET', 'USB', 'CPRI', 'WDC', 'OVV', 'SNY', 'W', 'PFGC', 'MOS', 'TTE', 'AIG', 'C', 'VTR', 'DOW', 'MAS', 'BUD', 'NVAX', 'CAH', 'SIG', 'COIN', 'DVN', 'PVH'
#             , 'OKE', 'TJX', 'GILD', 'MET', 'REGI', 'MU', 'OXY', 'MDLZ', 'KO', 'JD', 'WYNN', 'EIX', 'DOCU', 'SCHW', 'HIG', 'CLR', 'OMC', 'NTAP', 'MTCH', 'BALL', 'BBY', 'SO', 'SQ', 'BMY', 'ORCL', 'HAS', 'STX', 'DHI', 'ROST', 'D', 'ADM', 'ATVI', 'INCY', 'FSLR', 'NEE', 'SBUX', 'MS', 'H', 'TWLO']


"""  3 0 0 """

# print(Str3_0_0('^GSPC', share_tick1).signals())
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
# print(Str3_1_1('^GSPC', 'HEAR').get_table())
# print(Str3_1_1('^GSPC', 'HEAR', interval='1wk').get_table())


"""  4 0 0 """

# print(Str4_0_0('^GSPC', 'T').get_table())
# print(Str4_0_0(mt, share_tick).sum_results())
# print(Str4_0_0(mt, val_all_usd).sum_results())

"""  4 1 1 """
# print(int(Str4_1_1('^GSPC', share_tick1, stime='2018-05-01', ftime='2020-01-01', interval='1wk').sum_results()))
# print(int(Str4_1_1('^GSPC', share_tick1a, stime='2019-05-01', ftime='2020-06-01', interval='1wk').sum_results()))
# print(int(Str4_1_1('^GSPC', share_tick1b, stime='2019-10-01', ftime='2021-01-01', interval='1wk').sum_results()))

# print(int(Str4_1_1('^GSPC', val_all_usd, stime='2020-05-01', ftime='2021-10-01', interval='1wk').sum_results()))
# print(Str4_1_1('^GSPC', share_tick1cc, stime='2020-05-01', ftime='2021-10-01', interval='1wk').get_counts())
# print(int(Str4_1_1('^GSPC', val_all_usd, stime='2021-06-01', ftime='2022-04-03', interval='1wk').sum_results()))
# print(Str4_1_1('^GSPC', val_all_usd, stime='2021-06-01', ftime='2022-04-03', interval='1wk').get_counts())
# print(int(Str4_1_1('^GSPC', val_all_usd, stime='2022-01-01', interval='1wk').sum_results()))
# print(Str4_1_1('^GSPC', val_all_usd, stime='2022-01-01', interval='1wk').get_counts())

#
# print(int(Str4_1_1('^GSPC', p2_a, stime='2018-05-01', ftime='2020-01-01', interval='1wk').sum_results()))
# print(int(Str4_1_1('^GSPC', p2_b, stime='2019-05-01', ftime='2020-06-01', interval='1wk').sum_results()))
# print(int(Str4_1_1('^GSPC', p2_c, stime='2019-10-01', ftime='2021-01-01', interval='1wk').sum_results()))
# print(int(Str4_1_1('^GSPC', p2_d, stime='2020-05-01', ftime='2021-10-01', interval='1wk').sum_results()))
# print(int(Str4_1_1('^GSPC', p2_e, stime='2021-06-01', ftime='2022-04-03', interval='1wk').sum_results()))
# print(int(Str4_1_1('^GSPC', p2_f, stime='2022-01-01', interval='1wk').sum_results()))



# print(int(Str4_1_1('^GSPC', val_long_usd, stime='2019-05-01', ftime='2021-01-01', interval='1wk').sum_results()))
# print(int(Str4_1_1('^GSPC', val_long_usd, stime='2020-05-01', ftime='2022-01-01', interval='1wk').sum_results()))
# print(int(Str4_1_1('^GSPC', val_long_usd, stime='2021-06-01', ftime='2022-08-03', interval='1wk').sum_results()))
# print(int(Str4_1_1('^GSPC', ['cfg', 'intc'], stime='2022-01-01',  interval='1wk').sum_results()))
# print(int(Str4_1_1('^GSPC', ['aple', 'T'], stime='2020-01-01', ftime='2022-08-03', interval='1wk').sum_results()))


# print(Str4_1_1('^GSPC', ['aple', 'T'], stime='2022-01-01', ftime='2022-07-22',  interval='1wk').signals())
# print(Str4_1_1('^GSPC', val_long_usd, stime='2022-01-01',  interval='1wk').signals_without_gap())



# print(Str4_1_1('^GSPC', val_all_usd, stime='2022-01-01',  interval='1wk').signals_without_gap())

# print(Str4_1_1('^GSPC', 'aple', stime='2018-05-01', interval='1wk').get_table())

# print(int(Str4_1_1('^GSPC', p_a, stime='2018-05-01', ftime='2020-01-01', interval='1wk').sum_results()))
# print(int(Str4_1_1('^GSPC', p_b, stime='2019-05-01', ftime='2020-06-01', interval='1wk').sum_results()))
# print(int(Str4_1_1('^GSPC', p_c, stime='2019-10-01', ftime='2021-01-01', interval='1wk').sum_results()))
# print(int(Str4_1_1('^GSPC', p_d, stime='2020-05-01', ftime='2021-10-01', interval='1wk').sum_results()))
# # print(Str4_2_2('^GSPC', val_all_usd, stime='2020-05-01', ftime='2021-10-01', interval='1wk').get_counts())
# print(int(Str4_1_1('^GSPC', p_e, stime='2021-06-01', ftime='2022-04-03', interval='1wk').sum_results()))
# # print(Str4_2_2('^GSPC', val_all_usd, stime='2021-06-01',  ftime='2022-04-03', interval='1wk').get_counts())
# print(int(Str4_1_1('^GSPC', p_f, stime='2022-01-01', interval='1wk').sum_results()))






"""  4 2 2 """

# print(int(Str4_2_2('^GSPC', sec_share_tick1c, stime='2020-05-01', ftime='2021-10-01', interval='1wk').sum_results()))
# print(Str4_2_2('^GSPC', sec_share_tick1cc, stime='2020-05-01', ftime='2021-10-01', interval='1wk').get_counts())
# print(int(Str4_2_2('^GSPC', sec_share_tick1d, stime='2021-06-01', ftime='2022-04-03', interval='1wk').sum_results()))
# print(Str4_2_2('^GSPC', sec_share_tick1dd, stime='2021-06-01', ftime='2022-04-03', interval='1wk').get_counts())
# print(int(Str4_2_2('^GSPC', sec_share_tick1e, stime='2022-01-01', interval='1wk').sum_results()))
# print(Str4_2_2('^GSPC', sec_share_tick1ee, stime='2022-01-01', interval='1wk').get_counts())

# print(Str4_2_2('^GSPC', p_a, stime='2018-05-01', ftime='2020-01-01', interval='1wk').sum_results())
# print(Str4_2_2('^GSPC', p_b, stime='2019-05-01', ftime='2020-06-01', interval='1wk').sum_results())
# print(Str4_2_2('^GSPC', p_c, stime='2019-10-01', ftime='2021-01-01', interval='1wk').sum_results())
# print(Str4_2_2('^GSPC', p_d, stime='2020-05-01', ftime='2021-10-01', interval='1wk').sum_results())
# # print(Str4_2_2('^GSPC', val_all_usd, stime='2020-05-01', ftime='2021-10-01', interval='1wk').get_counts())
# print(Str4_2_2('^GSPC', p_e, stime='2021-06-01', ftime='2022-04-03', interval='1wk').sum_results())
# # print(Str4_2_2('^GSPC', val_all_usd, stime='2021-06-01',  ftime='2022-04-03', interval='1wk').get_counts())
# # print(int(Str4_2_2('^GSPC', p_f, stime='2022-01-01', interval='1wk').sum_results()))


# print(int(Str4_2_2('^GSPC', p2_a, stime='2018-05-01', ftime='2020-01-01', interval='1wk').sum_results()))
# print(int(Str4_2_2('^GSPC', p2_b, stime='2019-05-01', ftime='2020-06-01', interval='1wk').sum_results()))
# print(int(Str4_2_2('^GSPC', p2_c, stime='2019-10-01', ftime='2021-01-01', interval='1wk').sum_results()))
# print(int(Str4_2_2('^GSPC', p2_d, stime='2020-05-01', ftime='2021-10-01', interval='1wk').sum_results()))
# # print(Str4_2_2('^GSPC', val_all_usd, stime='2020-05-01', ftime='2021-10-01', interval='1wk').get_counts())
# print(int(Str4_2_2('^GSPC', p2_e, stime='2021-06-01', ftime='2022-04-03', interval='1wk').sum_results()))
# # print(Str4_2_2('^GSPC', val_all_usd, stime='2021-06-01',  ftime='2022-04-03', interval='1wk').get_counts())
# print(int(Str4_2_2('^GSPC', p2_f, stime='2022-01-01', interval='1wk').sum_results()))

xa = ['APLE', 'BAC', 'AAL', 'ABT', 'ALB']
xb = ['APLE', 'BAC', 'AAL', 'ABT', 'ALB']
xc = ['APLE', 'BAC', 'AAL', 'ABT', 'ALB']
xd = ['APLE', 'BAC', 'AAL', 'ABT', 'ALB']
xe = ['APLE', 'BAC', 'AAL', 'ABT', 'ALB']
xf = ['APLE', 'BAC', 'AAL', 'ABT', 'ALB']


# print(int(Str4_2_2('^GSPC', xa, stime='2018-05-01', ftime='2020-01-01', interval='1wk').sum_results()))
# print(int(Str4_2_2('^GSPC', xb, stime='2019-05-01', ftime='2020-06-01', interval='1wk').sum_results()))
# print(int(Str4_2_2('^GSPC', xc, stime='2019-10-01', ftime='2021-01-01', interval='1wk').sum_results()))
# print(int(Str4_2_2('^GSPC', xd, stime='2020-05-01', ftime='2021-10-01', interval='1wk').sum_results()))
# # print(Str4_2_2('^GSPC', xe, stime='2020-05-01', ftime='2021-10-01', interval='1wk').get_counts())
# print(int(Str4_2_2('^GSPC', xe, stime='2021-06-01', ftime='2022-04-03', interval='1wk').sum_results()))
# # print(Str4_2_2('^GSPC', 'APLE', stime='2021-06-01',  ftime='2022-04-03', interval='1wk').get_counts())
# print(Str4_2_2('^GSPC', val_all_usd, stime='2022-01-01', interval='1wk').sum_results())

# print(Str4_2_2('^GSPC', ['aple', 't'], stime='2022-01-01', interval='1wk').signals_without_gap())


"""SNP"""

print(Str4_2_2('^GSPC',   snp_b_15, stime='2018-05-01', ftime='2020-01-01', interval='1wk').sum_results())
print(Str4_2_2('^GSPC', snp_b_15a, stime='2019-05-01', ftime='2020-06-01', interval='1wk').sum_results())
print(Str4_2_2('^GSPC', snp_b_15b, stime='2019-10-01', ftime='2021-01-01', interval='1wk').sum_results())
print(Str4_2_2('^GSPC', snp_b_15c, stime='2020-05-01', ftime='2021-10-01', interval='1wk').sum_results())
# # print(Str4_2_2('^GSPC', xe, stime='2020-05-01', ftime='2021-10-01', interval='1wk').get_counts())
print(Str4_2_2('^GSPC', snp_b_15d, stime='2021-06-01', ftime='2022-04-03', interval='1wk').sum_results())
# print(Str4_2_2('^GSPC', 'APLE', stime='2021-06-01',  ftime='2022-04-03', interval='1wk').get_counts())
print(Str4_2_2('^GSPC', snp_b_15e, stime='2022-01-01', interval='1wk').sum_results())