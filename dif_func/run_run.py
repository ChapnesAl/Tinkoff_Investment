import pandas as pd
from sql_investi.sql_str_tests import Db_str_tests
from result_mdl.play_ground_str1 import Str1_0_0, Str1_0_1
from result_mdl.play_ground_str3 import Str3_0_0, Str3_0_1, Str3_1_1
from result_mdl.play_ground_str4 import Str4_0_0, Str4_1_1, Str4_2_2
from paper_filter.lists_papers import val_all_usd, val_long_usd, val_long_rub, val_all_rub
from tickers import snp_b2, snp_b2a, snp_b2b, snp_b2c, snp_b2d, snp_b2e
from tickers import snp_b_15_2, snp_b_15_2a, snp_b_15_2b, snp_b_15_2c, snp_b_15_2d, snp_b_15_2e
from tickers import snp_b_13_15, snp_b_13_15a, snp_b_13_15b, snp_b_13_15c, snp_b_13_15d, snp_b_13_15e
from tickers import snp_b_11_13, snp_b_11_13a, snp_b_11_13b, snp_b_11_13c, snp_b_11_13d, snp_b_11_13e
from tickers import snp_b_09_11, snp_b_09_11a, snp_b_09_11b, snp_b_09_11c, snp_b_09_11d, snp_b_09_11e
from tickers import b_15_plus, b_15_plus_a, b_15_plus_b, b_15_plus_c, b_15_plus_d, b_15_plus_e


""" Import Strategy Option"""
from strategies.str_options import p1_m1, p2_m1, p3_m1, p4_m1, p5_m1, p6_m1, p7_mr, p8_mr, p9_mr, p10_mr,\
     mrAM_MmrB15_a_mrAM1_a_mrBL05, p1_l1, p2_l1, p3_l1, p4_l1, p5_l1, p6_l1, p7_lr, p8_lr, p9_lr

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

mt = '^GSPC'  # '^GSPC', '^IXIC', '^RUT', '^DJI'
st = 'T'

snp_b_15 = ['COTY', 'CCL', 'JWN', 'DXC', 'HAL', 'SLB', 'RCL', 'BFH', 'DVN', 'OXY', 'WYNN', 'PVH', 'GPS', 'XRX', 'BKR',
            'PARA', 'FCX', 'ALK', 'WDC', 'C', 'MOS', 'OKE', 'DHI', 'BBY', 'MPC', 'AMD', 'PRU', 'EXPE', 'EOG', 'VLO',
            'MAR', 'HCA', 'ALB']





""" Str 1 0 0"""


# print(Str1_0_0('^GSPC', b_15_plus, stime='2022-01-01', interval='1d').signals_without_gap())
# print(Str1_0_0('^GSPC', val_long_usd, stime='2022-01-01', interval='1wk').signals_without_gap())
# print(Str1_0_0('^GSPC', 'aple', stime='2022-01-01', ftime='2022-08-14', interval='1wk').get_table())
# print(Str1_0_0('^GSPC', 'aapl', stime='2022-01-01', ftime='2022-08-13', interval='1wk').get_table())
# print(Str1_0_0('^GSPC', 'gthx', stime='2022-01-01', interval='1wk').get_table())
# print(Str1_0_0('^GSPC', 'gthx', stime='2022-01-01', interval='1wk').signals_without_gap())


# def for_test(st_o):
#     a = Str1_0_0('^GSPC', snp_b_15, stime='2018-05-01', ftime='2020-01-01', interval='1wk', str_opt=st_o).sum_results()
#     b = Str1_0_0('^GSPC', snp_b_15a, stime='2019-05-01', ftime='2020-06-01', interval='1wk', str_opt=st_o).sum_results()
#     c = Str1_0_0('^GSPC', snp_b_15b, stime='2019-10-01', ftime='2021-01-01', interval='1wk', str_opt=st_o).sum_results()
#     d = Str1_0_0('^GSPC', snp_b_15c, stime='2020-05-01', ftime='2021-10-01', interval='1wk', str_opt=st_o).sum_results()
#     e = Str1_0_0('^GSPC', snp_b_15d, stime='2021-06-01', ftime='2022-04-03', interval='1wk', str_opt=st_o).sum_results()
#     f = Str1_0_0('^GSPC', snp_b_15e, stime='2022-01-01', interval='1wk', str_opt=st_o).sum_results()
#
#     return a, b, c, d, e, f, st_o


def for_test(slist, st_o):
    s1 = list(slist)
    s2 = list(slist)
    s3 = list(slist)
    s4 = list(slist)
    s5 = list(slist)
    s6 = list(slist)
    a = Str1_0_0('^GSPC', s1, stime='2018-05-01', ftime='2020-01-01', interval='1wk', str_opt=st_o).sum_results()
    b = Str1_0_0('^GSPC', s2, stime='2019-05-01', ftime='2020-06-01', interval='1wk', str_opt=st_o).sum_results()
    c = Str1_0_0('^GSPC', s3, stime='2019-10-01', ftime='2021-01-01', interval='1wk', str_opt=st_o).sum_results()
    d = Str1_0_0('^GSPC', s4, stime='2020-05-01', ftime='2021-10-01', interval='1wk', str_opt=st_o).sum_results()
    e = Str1_0_0('^GSPC', s5, stime='2021-06-01', ftime='2022-04-03', interval='1wk', str_opt=st_o).sum_results()
    f = Str1_0_0('^GSPC', s6, stime='2022-01-01', interval='1wk', str_opt=st_o).sum_results()

    return a, b, c, d, e, f, st_o


def pack_analyse(slist, pack_st_op):
    l = list(pack_st_op)
    for i in range(len(pack_st_op)):
        l[i] = for_test(slist, pack_st_op[i])
    return tuple(l)


# print(pack_analyse(snp_b_15, p1_m1))

# a = ['2570', '270']
# aa = ['2570', '270']
# print(id(a))
# print(id(aa))

# Db_str_tests().insert_line_data(for_test(snp_b_15, mrAM_MmrB15_a_mrAM1_a_mrBL05))
Db_str_tests().insert_pack_data(pack_analyse(snp_b_15, p4_l1))
# Db_str_tests().del_all()
# Db_str_tests().create_table()
# Db_str_tests().get_full_table()


# print((Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2018-05-01', ftime='2020-01-01', interval='1wk', str_opt=m1_m).sum_results()))


# def for_test(st_o):
#     a = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2018-05-01', ftime='2020-01-01', interval='1wk', str_opt=st_o).sum_results()
#     b = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2019-05-01', ftime='2020-06-01', interval='1wk', str_opt=st_o).sum_results()
#     c = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2019-10-01', ftime='2021-01-01', interval='1wk', str_opt=st_o).sum_results()
#     d = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2020-05-01', ftime='2021-10-01', interval='1wk', str_opt=st_o).sum_results()
#     e = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2021-06-01', ftime='2022-04-03', interval='1wk', str_opt=st_o).sum_results()
#     f = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2022-01-01', interval='1wk', str_opt=st_o).sum_results()
#
#     def get_var_name(var):
#         for name in globals():
#             if eval(name) == var:
#                 return name
#     name = get_var_name(st_o)
#     return name, a, b, c, d, e, f
#
# print(for_test(a1))

# print(for_test(a1))
# print(Str1_0_0('^GSPC',  'AAPL', stime='2018-05-01', ftime='2020-01-01', interval='1wk', str_opt=a1).get_table())
# print(Str1_0_0('^GSPC',   b_15_plus, stime='2018-05-01', ftime='2020-01-01', interval='1wk', str_opt=a1).sum_results())

""" Str 1 0 1"""


# def for_test(st_o):
#     a = Str1_0_1('^GSPC',   b_15_plus, stime='2018-05-01', ftime='2020-01-01', interval='1d').sum_results()
#     b = Str1_0_1('^GSPC', b_15_plus_a, stime='2019-05-01', ftime='2020-06-01', interval='1d').sum_results()
#     c = Str1_0_1('^GSPC', b_15_plus_b, stime='2019-10-01', ftime='2021-01-01', interval='1d').sum_results()
#     d = Str1_0_1('^GSPC', b_15_plus_c, stime='2020-05-01', ftime='2021-10-01', interval='1d').sum_results()
#     e = Str1_0_1('^GSPC', b_15_plus_d, stime='2021-06-01', ftime='2022-04-03', interval='1d').sum_results()
#     f = Str1_0_1('^GSPC', b_15_plus_e, stime='2022-01-01', interval='1d').sum_results()
#     return a, b, c, d, e, f

