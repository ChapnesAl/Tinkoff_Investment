
from dif_func.companies_list import get_tick_figi


def ins_tinc_tic(connect):
    with connect.cursor() as cursor:
        y = get_tick_figi()
        for i in y:
            cursor.execute(
                f"""INSERT INTO tickers (ticker, figi)
                VALUES {i}"""
            )
        print("[INFO] Data was successfully inserted")



if __name__ == '__main__':
    print(get_tick_figi())