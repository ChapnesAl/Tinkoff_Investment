from strategies.str3.table_3_0 import ts3_0


def en_3_0_1(table):
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

                if gf_copy.iloc[ind[i], 4] > 0 and gf_copy.iloc[ind[i], 4] < 2 \
                        and gf_copy.iloc[ind[i] - 1, 4] > 2.5 and gf_copy.iloc[ind[i] - 1, 4] < 10 \
                        and gf_copy.iloc[ind[i] - 2, 4] > 5 and gf_copy.iloc[ind[i] - 2, 4] < 15 \
                        and gf_copy.iloc[ind[i] - 3, 4] > 0 and gf_copy.iloc[ind[i] - 3, 4] < 25 \
                        and gf_copy.iloc[ind[i] - 4, 4] > 0 and gf_copy.iloc[ind[i] - 4, 4] < 20 \
                        and gf_copy.iloc[ind[i] - 5, 4] < 20 \
                        and gf_copy.iloc[ind[i], 3] < 4:
                    r[i] = 'Short'
                elif gf_copy.iloc[ind[i], 4] < 0 and gf_copy.iloc[ind[i], 4] > -2 \
                        and gf_copy.iloc[ind[i] - 1, 4] < -2.5 and gf_copy.iloc[ind[i] - 1, 4] > -30 \
                        and gf_copy.iloc[ind[i] - 2, 4] < 5 and gf_copy.iloc[ind[i] - 2, 4] > -40 \
                        and gf_copy.iloc[ind[i] - 3, 4] < -1 and gf_copy.iloc[ind[i] - 3, 4] > -30 \
                        and gf_copy.iloc[ind[i] - 4, 4] < 10 \
                        and gf_copy.iloc[ind[i], 3] > -10:

                    r[i] = 'Long'
                else:
                    r[i] = '0'
            except:
                r[i] = '0'
        return r

        # def signal_to_deal(table, ind, tick):
        #     """ Long only"""
        #     gf_copy = table.copy(deep=True)
        #     gf_copy = gf_copy.astype({tick: str}, errors='ignore')
        #     r = gf_copy[tick].values
        #
        #     for i in range(len(ind)):
        #         try:
        #
        #             if gf_copy.iloc[ind[i], 4] < 0 and gf_copy.iloc[ind[i], 4] > -2 \
        #                     and gf_copy.iloc[ind[i] - 1, 4] < -2.5 and gf_copy.iloc[ind[i] - 1, 4] > -30 \
        #                     and gf_copy.iloc[ind[i] - 2, 4] < 5 and gf_copy.iloc[ind[i] - 2, 4] > -40 \
        #                     and gf_copy.iloc[ind[i] - 3, 4] < -1 and gf_copy.iloc[ind[i] - 3, 4] > -30 \
        #                     and gf_copy.iloc[ind[i] - 4, 4] < 10 \
        #                     and gf_copy.iloc[ind[i], 3] > -10:
        #                 # and gf_copy.iloc[ind[i] - 5, 4] < 20:
        #                 r[i] = 'Long'  # sell
        #                 # r[i] = 2
        #             else:
        #                 r[i] = '0'
        #                 # r[i] = 0
        #         except:
        #             r[i] = '0'
        #             # r[i] = 0
        #     return r

    gf["Signal"] = entrance(gf, index, stock_ticker)

    def result_of_strategy(table, ind, tick):
        gf_copy = table.copy(deep=True)
        t = gf_copy[tick].values
        for i in range(len(ind)):
            try:
                if gf_copy.iloc[ind[i], 5] == 'Long':
                    t[i] = gf_copy.iloc[ind[i] + 1, 3]
                    t[i] = gf_copy.iloc[ind[i] + 2, 3]
                    t[i] = gf_copy.iloc[ind[i] + 3, 3]
                    t[i] = gf_copy.iloc[ind[i] + 4, 3]
                    t[i] = gf_copy.iloc[ind[i] + 5, 3]
                    t[i] = gf_copy.iloc[ind[i] + 6, 3]
                    t[i] = gf_copy.iloc[ind[i] + 7, 3]
                    t[i] = gf_copy.iloc[ind[i] + 8, 3]
                    t[i] = gf_copy.iloc[ind[i] + 9, 3]
                    t[i] = gf_copy.iloc[ind[i] + 10, 3]
                    t[i] = gf_copy.iloc[ind[i] + 11, 3]
                    t[i] = gf_copy.iloc[ind[i] + 12, 3]
                    t[i] = gf_copy.iloc[ind[i] + 13, 3]
                    t[i] = gf_copy.iloc[ind[i] + 14, 3]
                    t[i] = gf_copy.iloc[ind[i] + 15, 3]
                    t[i] = gf_copy.iloc[ind[i] + 16, 3]
                    t[i] = gf_copy.iloc[ind[i] + 17, 3]
                    t[i] = gf_copy.iloc[ind[i] + 18, 3]
                    t[i] = gf_copy.iloc[ind[i] + 19, 3]
                    t[i] = gf_copy.iloc[ind[i] + 20, 3]
                    t[i] = gf_copy.iloc[ind[i] + 21, 3]
                elif gf_copy.iloc[ind[i], 5] == 'Short':
                    t[i] = gf_copy.iloc[ind[i] + 1, 3] * -1  # sell
                else:
                    t[i] = 0
            except:
                t[i] = 0

        return t

    gf["Results"] = result_of_strategy(gf, index, stock_ticker)

    return gf



if __name__ == '__main__':
    print(en_3_0_1(ts3_0('^GSPC','T')))