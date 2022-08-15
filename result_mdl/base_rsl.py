import pandas as pd
from get_tables.table_str3 import ts3

t1 = '^GSPC'
t2 = 'HPE'


class Base_mdl:

    def __init__(self, table):
        self.table = table

    def rt2(self):
        """All table and sum of result"""
        return self.table['Results'].sum()

    def deals_counts(self):
        self.table = self.table[(self.table.Signal == 'Long') | (self.table.Signal == 'Short')]
        return len(self.table['Signal'].values)



    def signal1(self):
        gf_copy = self.table.copy(deep=True)
        if gf_copy.iloc[-2, 6] == 'Long':
            a = 'Buy'
        elif gf_copy.iloc[-2, 6] == 'Short':
            a = 'Sell'
        else:
            return
        return a

    def signal2(self):
        gf_copy = self.table.copy(deep=True)
        w = self.table.loc['2022-07-01':'2022-07-30']
        e = w['Results'].sum()
        if gf_copy.iloc[-2, 6] == 'Long' and e < 6 and e > -6:
            a = 'Buy'
        elif gf_copy.iloc[-2, 6] == 'Long' and e <= -6:
            a = 'Buy-2'
        elif gf_copy.iloc[-2, 6] == 'Short' and e < 6 and e > -6:
            a = 'Sell'
        elif gf_copy.iloc[-2, 6] == 'Short' and e <= -6:
            a = 'Sell-2'
        else:
            return
        return a



    def date_sum2(self):
        """ THIS METHOD WORKS WITHOUT CURRENT LUST MONTH"""
        i = 1
        u = []
        while i < 12:
            x = f'2021-{i}-01'
            y31 = f'2021-{i}-31'
            y30 = f'2021-{i}-30'
            y29 = f'2021-{i}-29'
            y28 = f'2021-{i}-28'
            # print(self.table.loc[x:y])
            try:
                q = self.table.loc[x:y31]
            except:
                try:
                    q = self.table.loc[x:y30]
                except:
                    try:
                        q = self.table.loc[x:y29]
                    except:
                        try:
                            q = self.table.loc[x:y28]
                        except:
                            pass
            u.append(q['Results'].sum())
            i += 1
        else:
            q = self.table.loc['2021-12-01':'2022-01-01']
            # print(self.table.loc['2021-12-01':'2022-01-01'])
            u.append(q['Results'].sum())
        y = 1
        try:
            while y < 7:
                x = f'2022-{y}-01'
                z31 = f'2022-{y}-31'
                z30 = f'2022-{y}-30'
                z29 = f'2022-{y}-29'
                z28 = f'2022-{y}-28'
                try:
                    q = self.table.loc[x:z31]
                except:
                    try:
                        q = self.table.loc[x:z30]
                    except:
                        try:
                            q = self.table.loc[x:z29]
                        except:
                            try:
                                q = self.table.loc[x:z28]
                            except:
                                pass
                # print(self.table.loc[x:z])
                u.append(q['Results'].sum())
                y += 1
        except:
            pass
        # return 'Метод вызывается без Print. Print встроен'
        return u
            # print(table.loc['2022-1-01':w])

    def del_any_months(self):
        df = pd.DataFrame(self.date_sum2())
        l = df.index.tolist()
        copy_df = df.copy(deep=True)
        for x in range(len(l)):
            if df.iloc[x, 0] > 6:
                try:
                    copy_df.at[x+1, 0] = 0
                except:
                    pass
            else:
                pass
        return copy_df[0].values


# date_sum2(ts2(t1, t2))
if __name__ == "__main__":
    x = Base_mdl(ts3(t1, t2))
    # print(x.date_sum2())
    # print(sum(x.date_sum2()))

    print(x.del_any_months())

    # print(x.signal2())


