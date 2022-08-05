from strategies.str4.table_4_1 import ts_4_1


def en_4_1(table):
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

                if gf_copy.iloc[ind[i], 5] > 0 and gf_copy.iloc[ind[i], 5] < 2 \
                        and gf_copy.iloc[ind[i] - 1, 5] > 2.5 and gf_copy.iloc[ind[i] - 1, 5] < 10 \
                        and gf_copy.iloc[ind[i] - 2, 5] > 5 and gf_copy.iloc[ind[i] - 2, 5] < 15 \
                        and gf_copy.iloc[ind[i] - 3, 5] > 0 and gf_copy.iloc[ind[i] - 3, 5] < 25 \
                        and gf_copy.iloc[ind[i] - 4, 5] > 0 and gf_copy.iloc[ind[i] - 4, 5] < 20 \
                        and gf_copy.iloc[ind[i] - 5, 5] < 20 \
                        and gf_copy.iloc[ind[i], 3] < 4\
                        and gf_copy.iloc[ind[i], 4] > -10 and gf_copy.iloc[ind[i], 4] < 4.5\
                        and gf_copy.iloc[ind[i] - 1, 4] < 4.5:
                    r[i] = 'Short'
                elif gf_copy.iloc[ind[i], 5] < 0 and gf_copy.iloc[ind[i], 5] > -2 \
                        and gf_copy.iloc[ind[i] - 1, 5] < -2.5 and gf_copy.iloc[ind[i] - 1, 5] > -30 \
                        and gf_copy.iloc[ind[i] - 2, 5] < 5 and gf_copy.iloc[ind[i] - 2, 5] > -40 \
                        and gf_copy.iloc[ind[i] - 3, 5] < -1 and gf_copy.iloc[ind[i] - 3, 5] > -30 \
                        and gf_copy.iloc[ind[i] - 4, 5] < 10 \
                        and gf_copy.iloc[ind[i], 3] > -10\
                        and gf_copy.iloc[ind[i], 4] < 1 and gf_copy.iloc[ind[i], 4] > -10:

                    r[i] = 'Long'
                else:
                    r[i] = '0'
            except:
                r[i] = '0'
        return r

    # def entrance(table, ind, tick):
    #     """ Long only"""
    #     gf_copy = table.copy(deep=True)
    #     gf_copy = gf_copy.astype({tick: str}, errors='ignore')
    #     r = gf_copy[tick].values
    #
    #     for i in range(len(ind)):
    #         try:
    #             if gf_copy.iloc[ind[i], 5] < 0 and gf_copy.iloc[ind[i], 5] > -2 \
    #                     and gf_copy.iloc[ind[i] - 1, 5] < -2.5 and gf_copy.iloc[ind[i] - 1, 5] > -30 \
    #                     and gf_copy.iloc[ind[i] - 2, 5] < 5 and gf_copy.iloc[ind[i] - 2, 5] > -40 \
    #                     and gf_copy.iloc[ind[i] - 3, 5] < -1 and gf_copy.iloc[ind[i] - 3, 5] > -30 \
    #                     and gf_copy.iloc[ind[i] - 4, 5] < 10 \
    #                     and gf_copy.iloc[ind[i], 3] > -10\
    #                     and gf_copy.iloc[ind[i], 4] < 2 and gf_copy.iloc[ind[i], 4] > -10:
    #                     r[i] = 'Long'  # sell
    #             else:
    #                 r[i] = '0'
    #         except:
    #             r[i] = '0'
    #     return r

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
            except:
                t[i] = 0

        return t

    gf["Results"] = result_of_strategy(gf, index, stock_ticker)

    return gf



if __name__ == '__main__':
    print(en_4_1(ts_4_1('^GSPC','T')))