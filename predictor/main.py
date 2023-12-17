import pandas as pd

from data_retrieval import get_data_from_database
from svr_model import predict_next_30_days
from plotting import plot_prediction


def get_sp500_list():
    sp500_stocks = pd.DataFrame()
    try:
        sp500_stocks = pd.read_html(
            "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        )[0]["Symbol"].tolist()
    except Exception as e:
        print(f"Error getting sp500 stock list: {e}")
    finally:
        return sp500_stocks


if __name__ == "__main__":
    try:
        sp500_stocks = get_sp500_list()
        user_stock_ticker = None
        while True:
            user_stock_ticker = input("Please enter the S&P 500 stock ticker: ").upper()
            if user_stock_ticker in sp500_stocks:
                break
            else:
                print("Invalid S&P 500 stock ticker")

        df = get_data_from_database(user_stock_ticker)
        df_pred = predict_next_30_days(df)
        plot_prediction(df, df_pred)
    except Exception as e:
        print(f"Error while running prediction: {e}")
