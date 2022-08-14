from strategies.str4.table_4_2 import ts_4_2


def en_4_2(table):
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

                elif gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1.5)\
                    and gf_copy.iloc[ind[i], 2] < 1:
                    r[i] = 'Short'

                elif gf_copy.iloc[ind[i], 4] < (gf_copy.iloc[ind[i] - 1, 4] - 0.5) \
                and gf_copy.iloc[ind[i], 4] > -1 and gf_copy.iloc[ind[i], 4] < 0:
                    r[i] = 'Short'

# !!!!!!

                # elif gf_copy.iloc[ind[i], 4] > (gf_copy.iloc[ind[i] - 1, 4] + 1.5) \
                #         and gf_copy.iloc[ind[i], 4] < 1 and gf_copy.iloc[ind[i], 4] > 0:
                #     r[i] = 'Short'

                elif gf_copy.iloc[ind[i], 2] < (gf_copy.iloc[ind[i] - 1, 2] - 1)\
                        and gf_copy.iloc[ind[i], 2] < 0.5 and gf_copy.iloc[ind[i], 2] > -1:
                    r[i] = 'Long'


                elif gf_copy.iloc[ind[i], 4] > (gf_copy.iloc[ind[i] - 1, 4] + 0.5)\
                    and gf_copy.iloc[ind[i], 4] > 1:
                    r[i] = 'Long'


                elif gf_copy.iloc[ind[i], 4] > (gf_copy.iloc[ind[i] - 1, 4] + 0.5) \
                and gf_copy.iloc[ind[i], 4] < 0 and gf_copy.iloc[ind[i], 4] > -10:
                    r[i] = 'Long'


                elif gf_copy.iloc[ind[i], 3] < (gf_copy.iloc[ind[i] - 1, 3] - 0.5) and  gf_copy.iloc[ind[i] - 1, 3] < (gf_copy.iloc[ind[i] - 2, 3])\
                and gf_copy.iloc[ind[i], 3] > -3 and gf_copy.iloc[ind[i], 3] < 1:
                    r[i] = 'Short'


                elif gf_copy.iloc[ind[i], 5] < (gf_copy.iloc[ind[i] - 1, 4] - 0.5) \
                and gf_copy.iloc[ind[i], 5] > -2 and gf_copy.iloc[ind[i], 5] < 2:
                    r[i] = 'Short'


                elif gf_copy.iloc[ind[i], 3] < (gf_copy.iloc[ind[i] - 1, 3] - 1) \
                        and gf_copy.iloc[ind[i], 3] < 0 and gf_copy.iloc[ind[i], 3] > -1:
                    r[i] = 'Long'


                elif gf_copy.iloc[ind[i], 3] < (gf_copy.iloc[ind[i] - 1, 3] - 1) \
                        and gf_copy.iloc[ind[i], 3] > 1 and gf_copy.iloc[ind[i], 3] < 8:
                    r[i] = 'Short'




                # elif gf_copy.iloc[ind[i], 5] < (gf_copy.iloc[ind[i] - 1, 4] - 0.5) \
                #         and gf_copy.iloc[ind[i], 5] > 2 and gf_copy.iloc[ind[i], 5] < 8:
                #     r[i] = 'Long'

                # elif gf_copy.iloc[ind[i], 4] < (gf_copy.iloc[ind[i] - 1, 4] - 0.5):
                #     r[i] = 'Long'

                # elif gf_copy.iloc[ind[i], 4] > (gf_copy.iloc[ind[i] - 1, 4] - 6) :
                #     r[i] = 'Long'


                # elif gf_copy.iloc[ind[i], 2] > (gf_copy.iloc[ind[i] - 1, 2] + 1) \
                #         and gf_copy.iloc[ind[i], 2] > -2:
                #     r[i] = 'Short'

                # elif gf_copy.iloc[ind[i], 3] > (gf_copy.iloc[ind[i] - 1, 3] + 3) and (gf_copy.iloc[ind[i] - 1, 3]) > (gf_copy.iloc[ind[i] - 2, 3] + 3):
                    # and gf_copy.iloc[ind[i], 3] < -0.5:
                    # r[i] = 'Short'

                # elif gf_copy.iloc[ind[i], 5] > 2 and gf_copy.iloc[ind[i], 5] < 2.5:   # 3+
                #     r[i] = 'Long'
                # elif gf_copy.iloc[ind[i], 2] > 0 and gf_copy.iloc[ind[i], 2] < 0.5:
                #     r[i] = 'Short'
                # elif gf_copy.iloc[ind[i], 4] > 1 and gf_copy.iloc[ind[i], 4] < 1.5:   # 3+
                #     r[i] = 'Long'
                # elif gf_copy.iloc[ind[i], 2] > -1 and gf_copy.iloc[ind[i], 2] < -0.5:
                #     r[i] = 'Long'
                # elif gf_copy.iloc[ind[i], 4] > 1.5 and gf_copy.iloc[ind[i], 4] < 2:   # 1+
                #     r[i] = 'Long'
                #elif f_copy.iloc[ind[i], 4] > -2.5 and gf_copy.iloc[ind[i], 4] < -2:   # 1+
                #     r[i] = 'Long'
                # elif gf_copy.iloc[ind[i], 5] > 2.5 and gf_copy.iloc[ind[i], 5] < 3:
                #     r[i] = 'Short'
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
                    t[i] = gf_copy.iloc[ind[i] + 1, 3]  # buy
                elif gf_copy.iloc[ind[i], 6] == 'Short':
                    t[i] = gf_copy.iloc[ind[i] + 1, 3] * -1  # sell
                else:
                    t[i] = 0
                #
                # if gf_copy.iloc[ind[i], 6] == 'Long':
                #     t[i] = gf_copy.iloc[ind[i] + 1, 3] # buy
                # elif gf_copy.iloc[ind[i], 6] == 'Short':
                #     t[i] = gf_copy.iloc[ind[i] + 1, 3] * -1  # sell
                # else:
                #     t[i] = 0
            except:
                t[i] = 0

        return t

    gf["Results"] = result_of_strategy(gf, index, stock_ticker)

    return gf



if __name__ == '__main__':
    print(en_4_2(ts_4_2('^GSPC','aple')))