import numpy
import pandas as pd


# from yahoo_t1_copy import gf, r_ac_des


def rt1(gf):  # = result type 1

    """ Get matches in coefficient """

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
    x = y.index[y['Deal'] == 'Yes'].tolist()


    def result_of_sr(df, x):
        # t = x
        # for i in range(len(x)):
        #     if df.iloc[x[i], 3] >= 0:
        #         t[i] = df.iloc[x[i] + 1, 3] + df.iloc[x[i] + 2, 3] + df.iloc[x[i] + 3, 3]
        #     else:
        #         t[i] = (df.iloc[x[i] + 1, 3] + df.iloc[x[i] + 2, 3] + df.iloc[x[i] + 3, 3]) * -1
        #         pass
        # return t

        t = x
        for i in range(len(x)):
            try:
                if df.iloc[x[i], 3] >= 0:
                    t[i] = df.iloc[x[i] + 2, 3] + df.iloc[x[i] + 3, 3]
                else:
                    t[i] = (df.iloc[x[i] + 2, 3] + df.iloc[x[i] + 3, 3]) * -1

                    pass
            except:
                t[i] = 0
        return t

    summ = result_of_sr(gf, x)
    summ = sum(summ)

    # print(r_ac_des) # average desynchronization
    # print(summ)  # result of strategy
    # print(result_of_sr(gf,x)) # full table
    # print()
    # print(gf)
    return summ


""" PULT"""
# rt1()
