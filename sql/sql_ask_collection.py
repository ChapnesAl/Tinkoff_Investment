connection = None


# def get_data():
#     r = """SElECT figi FROM tickers WHERE ticker = 'GGG';"""
#     return r

def get_data(connect):
    with connect.cursor() as cursor:
        cursor.execute(
            """SElECT figi FROM tickers WHERE ticker = 'GGG';"""
        )
        print(cursor.fetchone())

# print(get_data())