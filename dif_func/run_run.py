import pandas as pd
from sql_investi.sql_str_tests import Db_str_tests
from result_mdl.play_ground_str1 import Str1_0_0, Str1_0_1
from result_mdl.play_ground_str3 import Str3_0_0, Str3_0_1, Str3_1_1
from result_mdl.play_ground_str4 import Str4_0_0, Str4_1_1, Str4_2_2
from paper_filter.lists_papers import val_all_usd, val_long_usd, val_long_rub, val_all_rub
from datetime import datetime
from tickers import p_a, p_b, p_c, p_d, p_e, p_f
from tickers import p2_a, p2_b, p2_c, p2_d, p2_e, p2_f
from tickers import snp_b2, snp_b2a, snp_b2b, snp_b2c, snp_b2d, snp_b2e
from tickers import snp_b_15_2, snp_b_15_2a, snp_b_15_2b, snp_b_15_2c, snp_b_15_2d, snp_b_15_2e
from tickers import snp_b_13_15, snp_b_13_15a, snp_b_13_15b,  snp_b_13_15c, snp_b_13_15d, snp_b_13_15e
from tickers import snp_b_11_13,  snp_b_11_13a,  snp_b_11_13b, snp_b_11_13c, snp_b_11_13d, snp_b_11_13e
from tickers import snp_b_09_11, snp_b_09_11a, snp_b_09_11b, snp_b_09_11c, snp_b_09_11d, snp_b_09_11e
from tickers import b_15_plus, b_15_plus_a, b_15_plus_b, b_15_plus_c, b_15_plus_d, b_15_plus_e
from tickers import snp_b_15, snp_b_15a, snp_b_15b, snp_b_15c, snp_b_15d, snp_b_15e


""" Import Strategy Option"""
from strategies.str_options import p1_m1, m1_m, m1_m_m


pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

mt = '^GSPC' # '^GSPC', '^IXIC', '^RUT', '^DJI'
st = 'T'




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


# print(int(Str4_2_2('^GSPC', p_a, stime='2018-05-01', ftime='2020-01-01', interval='1wk').sum_results()))
# print(int(Str4_2_2('^GSPC', p_b, stime='2019-05-01', ftime='2020-06-01', interval='1wk').sum_results()))
# print(int(Str4_2_2('^GSPC', p_c, stime='2019-10-01', ftime='2021-01-01', interval='1wk').sum_results()))
# print(int(Str4_2_2('^GSPC', p_d, stime='2020-05-01', ftime='2021-10-01', interval='1wk').sum_results()))
# # print(Str4_2_2('^GSPC', xe, stime='2020-05-01', ftime='2021-10-01', interval='1wk').get_counts())
# print(int(Str4_2_2('^GSPC', p_f, stime='2021-06-01', ftime='2022-04-03', interval='1wk').sum_results()))
# # print(Str4_2_2('^GSPC', 'APLE', stime='2021-06-01',  ftime='2022-04-03', interval='1wk').get_counts())
# print(Str4_2_2('^GSPC', p_e, stime='2022-01-01', interval='1wk').sum_results())



"""With beta"""
#
# print(Str4_2_2('^GSPC',   b_15_plus, stime='2018-05-01', ftime='2020-01-01', interval='1wk').sum_results())
# print(Str4_2_2('^GSPC', b_15_plus_a, stime='2019-05-01', ftime='2020-06-01', interval='1wk').sum_results())
# print(Str4_2_2('^GSPC', b_15_plus_b, stime='2019-10-01', ftime='2021-01-01', interval='1wk').sum_results())
# print(Str4_2_2('^GSPC', b_15_plus_c, stime='2020-05-01', ftime='2021-10-01', interval='1wk').sum_results())
# # # print(Str4_2_2('^GSPC', xe, stime='2020-05-01', ftime='2021-10-01', interval='1wk').get_counts())
# print(Str4_2_2('^GSPC', b_15_plus_d, stime='2021-06-01', ftime='2022-04-03', interval='1wk').sum_results())
# # print(Str4_2_2('^GSPC', 'APLE', stime='2021-06-01',  ftime='2022-04-03', interval='1wk').get_counts())
# print(Str4_2_2('^GSPC', b_15_plus_e, stime='2022-01-01', interval='1wk').sum_results())



# print(Str4_2_2('^GSPC', b_15_plus, stime='2022-01-01', interval='1wk').signals_without_gap())
# print(Str4_2_2('^GSPC', val_long_usd, stime='2022-01-01', interval='1wk').signals_without_gap())
# print(Str4_2_2('^GSPC', 'aple', stime='2022-01-01', ftime='2022-08-14', interval='1wk').get_table())
# print(Str4_2_2('^GSPC', 'aapl', stime='2022-01-01', ftime='2022-08-13', interval='1wk').get_table())
# print(Str4_2_2('^GSPC', 'gthx', stime='2022-01-01', interval='1wk').get_table())
# print(Str4_2_2('^GSPC', 'gthx', stime='2022-01-01', interval='1wk').signals_without_gap())


""" Str 1 0 0"""

#
# print(Str1_0_0('^GSPC',   b_15_plus, stime='2018-05-01', ftime='2020-01-01', interval='1wk').sum_results())
# print(Str1_0_0('^GSPC', b_15_plus_a, stime='2019-05-01', ftime='2020-06-01', interval='1wk').sum_results())
# print(Str1_0_0('^GSPC', b_15_plus_b, stime='2019-10-01', ftime='2021-01-01', interval='1wk').sum_results())
# print(Str1_0_0('^GSPC', b_15_plus_c, stime='2020-05-01', ftime='2021-10-01', interval='1wk').sum_results())
# # # print(Str1_0_0('^GSPC', xe, stime='2020-05-01', ftime='2021-10-01', interval='1wk').get_counts())
# print(Str1_0_0('^GSPC', b_15_plus_d, stime='2021-06-01', ftime='2022-04-03', interval='1wk').sum_results())
# # print(Str4_2_2('^GSPC', 'APLE', stime='2021-06-01',  ftime='2022-04-03', interval='1wk').get_counts())
# print(Str1_0_0('^GSPC', b_15_plus_e, stime='2022-01-01', interval='1wk').sum_results())



# print(Str1_0_0('^GSPC', b_15_plus, stime='2022-01-01', interval='1d').signals_without_gap())
# print(Str1_0_0('^GSPC', val_long_usd, stime='2022-01-01', interval='1wk').signals_without_gap())
# print(Str1_0_0('^GSPC', 'aple', stime='2022-01-01', ftime='2022-08-14', interval='1wk').get_table())
# print(Str1_0_0('^GSPC', 'aapl', stime='2022-01-01', ftime='2022-08-13', interval='1wk').get_table())
# print(Str1_0_0('^GSPC', 'gthx', stime='2022-01-01', interval='1wk').get_table())
# print(Str1_0_0('^GSPC', 'gthx', stime='2022-01-01', interval='1wk').signals_without_gap())
#
# def for_test(st_o):
#     a = Str1_0_0('^GSPC',  snp_b_15, stime='2018-05-01', ftime='2020-01-01', interval='1wk', str_opt=st_o).sum_results()
#     b = Str1_0_0('^GSPC', snp_b_15a, stime='2019-05-01', ftime='2020-06-01', interval='1wk', str_opt=st_o).sum_results()
#     c = Str1_0_0('^GSPC', snp_b_15b, stime='2019-10-01', ftime='2021-01-01', interval='1wk', str_opt=st_o).sum_results()
#     d = Str1_0_0('^GSPC', snp_b_15c, stime='2020-05-01', ftime='2021-10-01', interval='1wk', str_opt=st_o).sum_results()
#     e = Str1_0_0('^GSPC', snp_b_15d, stime='2021-06-01', ftime='2022-04-03', interval='1wk', str_opt=st_o).sum_results()
#     f = Str1_0_0('^GSPC', snp_b_15e, stime='2022-01-01', interval='1wk', str_opt=st_o).sum_results()
#
#     def get_var_name(var):
#         for name in globals():
#             if eval(name) == var:
#                 return name
#     name = get_var_name(st_o)
#     return name, a, b, c, d, e, f

def for_test(st_o):
    a = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2018-05-01', ftime='2020-01-01', interval='1wk', str_opt=st_o).sum_results()
    b = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2019-05-01', ftime='2020-06-01', interval='1wk', str_opt=st_o).sum_results()
    c = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2019-10-01', ftime='2021-01-01', interval='1wk', str_opt=st_o).sum_results()
    d = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2020-05-01', ftime='2021-10-01', interval='1wk', str_opt=st_o).sum_results()
    e = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2021-06-01', ftime='2022-04-03', interval='1wk', str_opt=st_o).sum_results()
    f = Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2022-01-01', interval='1wk', str_opt=st_o).sum_results()

    # def get_var_name(var):
    #     for name in globals():
    #         if eval(name) == var:
    #             return name
    # name = get_var_name(st_o)
    return a, b, c, d, e, f, st_o

def pack_analyse(pack_st_op):
    l = list(pack_st_op)
    for i in range(len(pack_st_op)):
        l[i] = for_test(pack_st_op[i])
    return tuple(l)

Db_str_tests().insert_datas(for_test(m1_m))

# print(type(float(Str1_0_0('^GSPC', ['AAPL', 'T'], stime='2018-05-01', ftime='2020-01-01', interval='1wk', str_opt=m1_m).sum_results())))


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

# # print(Str1_0_1('^GSPC', xe, stime='2020-05-01', ftime='2021-10-01', interval='1d').get_counts())
# print(Str1_0_1('^GSPC', 'APLE', stime='2021-06-01',  ftime='2022-04-03', interval='1d').get_counts())

# def for_test(st_o):
#     a = Str1_0_1('^GSPC',   b_15_plus, stime='2018-05-01', ftime='2020-01-01', interval='1d').sum_results()
#     b = Str1_0_1('^GSPC', b_15_plus_a, stime='2019-05-01', ftime='2020-06-01', interval='1d').sum_results()
#     c = Str1_0_1('^GSPC', b_15_plus_b, stime='2019-10-01', ftime='2021-01-01', interval='1d').sum_results()
#     d = Str1_0_1('^GSPC', b_15_plus_c, stime='2020-05-01', ftime='2021-10-01', interval='1d').sum_results()
#     e = Str1_0_1('^GSPC', b_15_plus_d, stime='2021-06-01', ftime='2022-04-03', interval='1d').sum_results()
#     f = Str1_0_1('^GSPC', b_15_plus_e, stime='2022-01-01', interval='1d').sum_results()
#     return a, b, c, d, e, f
#
# print(for_test())

# print(Str1_0_1('^GSPC', b_15_plus, stime='2018-05-01', ftime='2020-01-01', interval='1d').sum_results())
# print(Str1_0_1('^GSPC', b_15_plus_a, stime='2019-05-01', ftime='2020-06-01', interval='1d').sum_results())
# print(Str1_0_1('^GSPC', b_15_plus_b, stime='2019-10-01', ftime='2021-01-01', interval='1d').sum_results())
# print(Str1_0_1('^GSPC', b_15_plus_c, stime='2020-05-01', ftime='2021-10-01', interval='1d').sum_results())
# print(Str1_0_1('^GSPC', b_15_plus_d, stime='2021-06-01', ftime='2022-04-03', interval='1d').sum_results())
# print(Str1_0_1('^GSPC', b_15_plus_e, stime='2022-01-01', interval='1d').sum_results())

# print(Str1_0_1('^GSPC', b_15_plus, stime='2022-01-01', interval='1d').signals_without_gap())
# print(Str1_0_1('^GSPC', val_long_usd, stime='2022-01-01', interval='1wk').signals_without_gap())
# print(Str1_0_1('^GSPC', 'aple', stime='2022-01-01', ftime='2022-08-14', interval='1wk').get_table())
# print(Str1_0_1('^GSPC', 'aapl', stime='2022-01-01', ftime='2022-08-13', interval='1wk').get_table())
# print(Str1_0_1('^GSPC', 'gthx', stime='2022-01-01', interval='1d').get_table())
# print(Str1_0_1('^GSPC', 'gthx', stime='2022-01-01', interval='1wk').signals_without_gap())