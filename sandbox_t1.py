import numpy
import pandas as pd
import yfinance as yf
from pprint import pprint
from yahoo_t1 import gf, r_ac_des




def find_1_plus_3_math(table):
    gf_copy = gf.copy(deep=True)
    gf_copy2 = gf.copy(deep=True)
    gf_copy = pd.DataFrame(gf_copy.drop(gf.index[0]))
    c = gf_copy['Coef'].values
    gf_copy2["Coef2"] = numpy.append(c, [None], axis=0)

    x = gf_copy2.query('Coef == 1.0 and Coef2 == 3.0')
    x = pd.DataFrame(x)
    x['Deal'] = 'Yes'

    return x['Deal']


gf['Deal'] = find_1_plus_3_math(gf)

change = gf["Deal"].values
change = numpy.insert(change, 0, 0)
change = numpy.delete(change, -1)
gf['Deal'] = change


y = gf.reset_index()
x = y.index[y['Deal'] =='Yes'].tolist()


# print(gf.iloc[3,4] + gf.iloc[4,4])

print(x, y)


def result_of_sr(df, x):
    t = x
    for i in range(len(x)):
        if df.iloc[x[i], 3] >= 0:
            t[i] = df.iloc[x[i]+1, 3] + df.iloc[x[i]+2, 3] + df.iloc[x[i]+3, 3]
        else:
            t[i] = (df.iloc[x[i] + 1, 3] + df.iloc[x[i] + 2, 3] + df.iloc[x[i] + 3, 3]) * -1
            pass
    return t




#
#
all_names = result_of_sr(gf,x)
summ = sum(all_names)



""" PULT"""
# print(r_ac_des) # average desynchronization
# print(all_names) # details of result
# print(summ)  # result of strategy


# print(gf) # full table
# print(x)
