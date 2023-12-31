from pymongo import MongoClient
import pandas as pd


def get_data_from_database(stock_ticker):
    print("Start get_data_from_database")
    df = pd.DataFrame()
    try:
        connection_string = "mongodb+srv://AdhamSakr:EDsxIryI4nhgtAHc@cluster0.mdltzjn.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(connection_string)
        db = client.sp500_db
        collection = db.sp500
        query = {"symbol": stock_ticker}
        projection = {"_id": 0}  # exclude mongodb's _id field from the result
        result = collection.find(query, projection)
        df = pd.DataFrame(list(result))
        df = drop_symbol_column(df)
        df = convert_date_to_index(df)
        df = drop_weakly_correlated_columns(df)
    except Exception as e:
        print(f"Error while getting data from database: {e}")
    finally:
        print("End get_data_from_database")
        return df


def drop_symbol_column(df):
    # Drop symbol column as it will be no longer useful
    df = df.drop(columns="symbol")
    return df


def convert_date_to_index(df):
    df = df.set_index(["date"])
    return df


def drop_weakly_correlated_columns(df):
    threshold = 0.5
    target_column = "close"
    correlation_coefficients = df.corr()[target_column]
    columns_to_drop = correlation_coefficients[
        abs(correlation_coefficients) < threshold
    ].index
    df = df.drop(columns=columns_to_drop)
    return df
