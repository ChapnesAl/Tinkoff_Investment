from result_mdl.play_ground_str3 import Str3_0_0
from result_mdl.play_ground_str3 import Str3_0_1
from result_mdl.play_ground_str4 import Str4_0_0
from paper_filter.lists_papers import val_all_usd, val_long_usd, val_long_rub, val_all_rub

mt = '^GSPC' # '^GSPC', '^IXIC', '^RUT', '^DJI'
st = 'T'
share_tick = ["HEAR", "SNAP", "TAK", "XRX", 'NTNX', 'HA', 'CLF', 'PLUG', 'ACAD', 'SHI', 'IVZ', 'M', 'WU', 'M', 'CNK', 'KMI', 'TRIP', 'LEVI', 'KEY', 'CHX', 'IBN', 'CHGG', 'RF', 'WB', 'JWN', 'LTHM', 'PINS', 'ANAB', 'T', 'UPWK', 'UBER', 'VREX', 'BJRI', 'BILI', 'SAVE', 'BEN', 'PARA', 'YY', 'FCX', 'BKR', 'RRC']


"""  3 0 0 """

# print(Str3_0_0('^GSPC', 'T').signals())
# print(Str3_0_0(mt, 'T').sum_results())
# print(Str3_0_0('^GSPC', 'T').get_table())
# print(Str3_0_0('^GSPC', 'T').month_results())
# print(Str3_0_0('^GSPC', ['T', 'AA']).month_results_without_bad())
# print(Str3_0_0('^GSPC', val_all_rub).sum_results_rus())
# print(Str3_0_0(mt, val_long_usd).sum_results())


"""  3 0 1 """

print(Str3_0_1(mt, val_all_usd).sum_results())

"""  4 0 0 """

# print(Str4_0_0('^GSPC', 'T').get_table())
# print(Str4_0_0(mt, share_tick).sum_results())
# print(Str4_0_0(mt, val_all_usd).sum_results())