from dif_func.companies_list import get_companies
import pandas as pd

# print(get_companies())

df = get_companies()

df_filt = df[(df.api_trade == True) & (df.short_enabled == True) & (df.currency == 'usd')]
df_filt2 = df[(df.api_trade == True) & (df.short_enabled == False) & (df.currency == 'usd')]
df_filt3 = df[(df.api_trade == True) & (df.short_enabled == True) & (df.currency == 'rub')]
df_filt4 = df[(df.api_trade == True) & (df.short_enabled == False) & (df.currency == 'rub')]


def get_all_rus(table):
    x = list(table['figi'].values)
    y = list(table['ticker'].values)
    for i in range(len(x)):
        x[i] = [x[i], y[i]]
    return x


val_all_usd = list(df_filt['ticker'].values)
val_long_usd = list(df_filt2['ticker'].values)
val_all_rub = get_all_rus(df_filt3)
val_long_rub = get_all_rus(df_filt4)


if __name__ == '__main__':
    # print(len(val_all_usd))
    # print(len(val_long_usd))
    # print(val_long_usd)
    print(val_all_rub)
    # print(val_long_rub)

    # print(df_filt3)
    # print(y)