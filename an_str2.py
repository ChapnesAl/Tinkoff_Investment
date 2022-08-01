from get_tables.table_str2 import ts2

t1 = '^GSPC'
t2 = 'LYFT'


# share_tick = ['AAL', 'ACN', 'ABBV', 'AA', 'AMD', 'APLE', 'NFLX', 'VEON', 'SLDB']
# share_tick = ['EAR', 'ZYNE', 'ASTR', 'BYSI', 'CORR', 'CRTX', 'CLOV', 'WKHS', 'HRTX', 'MFGP']
# share_tick = ['PBI', 'RKLB', 'CLSK', 'MOMO', 'RIOT', 'MLCO', 'LPL', 'SWN', 'GTHX', 'ETRN']
# share_tick = ['SPCE', 'GOSS', 'COTY', 'ZYXI', 'LFC', 'RRGB', 'ATRA', 'MARA',  'AERI', 'EHTH']
# share_tick = ['CCL', 'UAA', 'GPS', 'MAC', 'PUMP', 'ACH', 'ET', 'VIPS', 'PLTR', 'PTON']
# share_tick = ['PCG', 'OII', 'PAGS', 'GT', 'F', 'HBAN', 'IOVA', 'TWOU', 'HPE', 'LYFT']

def rt2(table):
    """All table and sum of result"""
    return table['Results'].sum()


def signal2(table):
    gf_copy = table.copy(deep=True)
    if gf_copy.iloc[-1, 5] == 1.0:
        a = 'Buy'
    elif gf_copy.iloc[-1, 5] == 2.0:
        a ='Sell'
    else:
        return
    return a


def date_sum2(table):
    i = 1
    while i < 12:
        x = f'2021-{i}-01'
        y = f'2021-{i+1}-01'
        # print(table.loc[x:y])
        q = table.loc[x:y]
        print(q['Results'].sum())
        i += 1
    else:
        q =table.loc['2021-12-01':'2022-01-01']
        print(q['Results'].sum())
    y = 1
    try:
        while y < 6:
            x = f'2022-{y}-01'
            z = f'2022-{y + 1}-01'
            q = table.loc[x:z]
            print(q['Results'].sum())
            y += 1
    except:
        q = f'{table.iloc[-1, 1]}'
        print(q['Results'].sum())

        # print(table.loc['2022-1-01':w])



# date_sum2(ts2(t1, t2))
if __name__ == "__main__":
   date_sum2(ts2(t1, t2))