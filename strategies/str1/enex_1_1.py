from strategies.str1.table_1_0 import ts_1_0

st_o = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] + 1, 2] - 0) and gf_copy.iloc[ind[i], 2] < 1000 and gf_copy.iloc[ind[i] - 1, 2] < 1000"
def en_1_1(table, s_o):
    gf = table
    stock_ticker = table.columns[1]
    def get_index(table):
        gf_copy = table.copy(deep=True)
        gf_copy = gf_copy.reset_index()
        gf_copy = gf_copy.index.tolist()
        return gf_copy

    index = get_index(gf)

    def entrance(table, ind, tick, s_o):
        """ Long and Short"""
        gf_copy = table.copy(deep=True)
        gf_copy = gf_copy.astype({tick: str}, errors='ignore')
        r = gf_copy[tick].values
        a = "gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] + 1, 2] - 0) and gf_copy.iloc[ind[i], 2] < 1000 and gf_copy.iloc[ind[i] - 1, 2] < 1000"
        for i in range(len(ind)):
            try:

                if gf_copy.iloc[ind[i], 3] in [gf_copy.iloc[0, 3], gf_copy.iloc[1, 3], gf_copy.iloc[2, 3],
                                               gf_copy.iloc[3, 3], gf_copy.iloc[4, 3], gf_copy.iloc[5, 3]]:
                    # r[i] = type(gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] + 1, 2] - 0) and gf_copy.iloc[ind[i], 2] < 1000 and gf_copy.iloc[ind[i] - 1, 2] < 1000)
                    r[i] = 0

                elif eval(s_o):
                    r[i] = 'Long'

                # elif gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] + 1, 2] - 0) and gf_copy.iloc[ind[i], 2] < 1000 and gf_copy.iloc[ind[i] - 1, 2] < 1000:
                #     r[i] = 'Long'

                # elif gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] + 1, 2] + 1) \
                #        and gf_copy.iloc[ind[i], 2] < 4\
                #         and gf_copy.iloc[ind[i] - 1, 2] < 0.5:
                #     r[i] = 'Long'

                # elif gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 2)\
                #         and gf_copy.iloc[ind[i], 2] < 0:
                #     r[i] = 'Short'

                else:
                    r[i] = '0'
            except:
                r[i] = '0'
        return r


    gf["Signal"] = entrance(gf, index, stock_ticker, s_o)

    def result_of_strategy(table, ind, tick):
        gf_copy = table.copy(deep=True)
        t = gf_copy[tick].values
        for i in range(len(ind)):
            try:

                if gf_copy.iloc[ind[i], 6] == 'Long':
                    t[i] = gf_copy.iloc[ind[i] + 2, 3] # buy
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
    print(en_1_1(ts_1_0('^GSPC', 'Aple', interval='1d'), st_o))