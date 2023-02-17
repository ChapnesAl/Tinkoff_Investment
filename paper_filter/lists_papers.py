from dif_func.companies_list import get_companies
import pandas as pd

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# print(get_companies())

df = get_companies()

df_filt = df[(df.api_trade == True) & (df.short_enabled == True) & (df.currency == 'usd')]
df_filt2 = df[(df.api_trade == True) & (df.short_enabled == False) & (df.currency == 'usd')]
df_filt3 = df[(df.api_trade == True) & (df.short_enabled == True) & (df.currency == 'rub')]
df_filt4 = df[(df.api_trade == True) & (df.short_enabled == False) & (df.currency == 'rub')]

# sector filters
df_energy = df[(df.sector == 'energy') & (df.currency == 'usd')]
df_health_care = df[(df.sector == 'health_care') & (df.currency == 'usd')]
df_financial = df[(df.sector == 'financial') & (df.currency == 'usd')]
df_it = df[(df.sector == 'it') & (df.currency == 'usd')]
df_consumer = df[(df.sector == 'consumer') & (df.currency == 'usd')]
df_materials = df[(df.sector == 'materials') & (df.currency == 'usd')]
df_industrials = df[(df.sector == 'industrials') & (df.currency == 'usd')]
df_telecom = df[(df.sector == 'telecom') & (df.currency == 'usd')]
df_ecomaterials = df[(df.sector == 'ecomaterials') & (df.currency == 'usd')]
df_real_estate = df[(df.sector == 'real_estate') & (df.currency == 'usd')]
df_utilities = df[(df.sector == 'utilities') & (df.currency == 'usd')]
df_electrocars = df[(df.sector == 'electrocars') & (df.currency == 'usd')]
df_green_energy = df[(df.sector == 'green_energy') & (df.currency == 'usd')]

# get tickers lists
energy_list = list(df_energy['ticker'].values)
health_care_list =  list(df_health_care['ticker'].values)
financial_list = list(df_financial['ticker'].values)
it_list = list(df_it['ticker'].values)
consumer_list = list(df_consumer['ticker'].values)
materials_list = list(df_materials['ticker'].values)
industrials_list = list(df_industrials['ticker'].values)
telecom_list = list(df_telecom['ticker'].values)
ecomaterials_list = list(df_ecomaterials['ticker'].values)
real_estate_list = list(df_real_estate['ticker'].values)
utilities_list = list(df_utilities['ticker'].values)
electrocars_list = list(df_electrocars['ticker'].values)
green_energy_list = list(df_green_energy['ticker'].values)







val_all_usd = list(df_filt['ticker'].values)
val_long_usd = list(df_filt2['ticker'].values)

def get_all_rus(table):
    x = list(table['figi'].values)
    y = list(table['ticker'].values)
    for i in range(len(x)):
        x[i] = [x[i], y[i]]
    return x

val_all_rub = get_all_rus(df_filt3)
val_long_rub = get_all_rus(df_filt4)


if __name__ == '__main__':
    # print(val_all_usd)
    # print(len(val_long_usd))
    # print(val_long_usd)
    # print(val_all_rub)
    # print(val_long_rub)

    # print(df_filt3)
    # print(y)
    # print(df.tail(30))
    print(real_estate_list)
