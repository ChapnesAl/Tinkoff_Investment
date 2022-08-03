from result_mdl.play_ground_str3 import Str3_0_0
from paper_filter.lists_papers import val_all_usd, val_long_usd, val_long_rub, val_all_rub

mt = '^GSPC'
st = 'T'


# print(Str3_0_0('^GSPC', 'T').signals())
print(Str3_0_0(mt, 'T').sum_results())
# print(Str3_0_0('^GSPC', 'T').get_table())
# print(Str3_0_0('^GSPC', 'T').month_results())
# print(Str3_0_0('^GSPC', ['T', 'AA']).month_results_without_bad())
# print(Str3_0_0('^GSPC', val_all_rub).sum_results_rus())

