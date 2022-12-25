from strategies.str1.table_1_0 import ts_1_0
from strategies.str_options_4column import m1_m




def cr_en_1_0(table):
    gf = table
    stock_ticker = table.columns[1]

    def get_index(table):
        gf_copy = table.copy(deep=True)
        gf_copy = gf_copy.reset_index()
        gf_copy = gf_copy.index.tolist()
        return gf_copy

    index = get_index(gf)

    def entrance(table, ind, tick):
        """ Long and Short"""
        gf_copy = table.copy(deep=True)
        gf_copy = gf_copy.astype({tick: str}, errors='ignore')
        r = gf_copy[tick].values

        for i in range(len(ind)):
            try:

                if gf_copy.iloc[ind[i], 3] in [gf_copy.iloc[0, 3], gf_copy.iloc[1, 3], gf_copy.iloc[2, 3],
                                               gf_copy.iloc[3, 3], gf_copy.iloc[4, 3], gf_copy.iloc[5, 3]]:
                    r[i] = 0

                elif gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 2):
                    r[i] = 'Long'


                elif gf_copy.iloc[ind[i], 2] > gf_copy.iloc[ind[i] - 1, 2] > gf_copy.iloc[ind[i] - 2, 2] > gf_copy.iloc[ind[i] - 3, 2]:
                    r[i] = 'Short'


                else:
                    r[i] = '0'
            except:
                r[i] = '0'
        return r


    gf["Signal"] = entrance(gf, index, stock_ticker)

    def result_of_strategy(table, ind, tick):
        gf_copy = table.copy(deep=True)
        t = gf_copy[tick].values
        for i in range(len(ind)):
            try:

                if gf_copy.iloc[ind[i], 6] == 'Long':
                    t[i] = gf_copy.iloc[ind[i] + 2, 3]  # buy
                elif gf_copy.iloc[ind[i], 6] == 'Short':
                    t[i] = gf_copy.iloc[ind[i] + 2, 3] * -1  # sell
                else:
                    t[i] = 0
            except:
                t[i] = 0

        return t

    gf["Results"] = result_of_strategy(gf, index, stock_ticker)

    return gf



if __name__ == '__main__':
    print(cr_en_1_0(ts_1_0('^GSPC', 'ACN', interval='1wk')))
    # print(m1_m)