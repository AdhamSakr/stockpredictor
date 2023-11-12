import pandas as pd


def merge_technical_fundamental_data(technical_df, fundamental_df):
    print("Start merge_technical_fundamental_data")
    sp500_df = pd.DataFrame()
    try:
        sp500_df = pd.merge(technical_df, fundamental_df, on=["Date", "Symbol"])
    except Exception as e:
        print(f"Error occured while merging technical and fundamental dataframes: {e}")
    finally:
        print("End merge_technical_fundamental_data")
        return sp500_df


def set_date_as_index(df):
    try:
        print("Start set_date_as_index")
        df = df.set_index(["Date"])
    except Exception as e:
        print(f"Error occured while setting date column as index: {e}")
    finally:
        print("End set_date_as_index")
        return df


def change_index_to_date_column(df):
    try:
        print("Start change_index_to_date_column")
        df.rename(columns={"index": "Date"}, inplace=True)
    except Exception as e:
        print(f"Error occured while changing index to date column: {e}")
    finally:
        print("End change_index_to_date_column")
        return df


def change_date_column_type(df):
    try:
        print("Start change_date_column_type")
        df["Date"] = pd.to_datetime(df["Date"])
    except Exception as e:
        print(f"Error occured while changing date column from object to datetime: {e}")
    finally:
        print("End change_date_column_type")
        return df


def reset_index(df):
    try:
        print("Start reset_index")
        df.reset_index(inplace=True)
    except Exception as e:
        print(f"Error occured while resetting dataframe index: {e}")
    finally:
        print("End reset_index")
        return df


def change_column_datatypes(sp500_df):
    print("Start change_column_datatypes")
    try:
        sp500_df["Basic EPS"] = sp500_df["Basic EPS"].astype("float64")
        sp500_df["Net Income"] = sp500_df["Net Income"].astype("float64")
        sp500_df["Total Revenue"] = sp500_df["Total Revenue"].astype("float64")
        sp500_df["Total Expenses"] = sp500_df["Total Expenses"].astype("float64")
        sp500_df["Total Debt"] = sp500_df["Total Debt"].astype("float64")
        sp500_df["Total Capitalization"] = sp500_df["Total Capitalization"].astype(
            "float64"
        )
        sp500_df["Total Assets"] = sp500_df["Total Assets"].astype("float64")
        sp500_df["Free Cash Flow"] = sp500_df["Free Cash Flow"].astype("float64")
        sp500_df["Capital Expenditure"] = sp500_df["Capital Expenditure"].astype(
            "float64"
        )
    except Exception as e:
        print(f"Error while converting data types of columns: {e}")
    finally:
        print("End change_column_datatypes")
        return sp500_df


def reorder_columns(sp500_df):
    print("Start reorder_columns")
    try:
        sp500_df = sp500_df[
            [
                "Symbol",
                "Open",
                "High",
                "Low",
                "Adj Close",
                "Volume",
                "Basic EPS",
                "Net Income",
                "Total Revenue",
                "Total Expenses",
                "Total Debt",
                "Total Capitalization",
                "Total Assets",
                "Free Cash Flow",
                "Capital Expenditure",
                "Close",
            ]
        ]
    except Exception as e:
        print(f"Error while reordering columns: {e}")
    finally:
        print("End reorder_columns")
        return sp500_df


def drop_null_values(df):
    print("Start drop_null_values")
    try:
        df.dropna(inplace=True)
    except Exception as e:
        print(f"Error while dropping null values: {e}")
    finally:
        print("End drop_null_values")
        return df


def drop_column(df, column_name):
    print("Start drop_column")
    try:
        df.drop(columns=column_name, inplace=True)
    except Exception as e:
        print(f"Error while dropping column {column_name}: {e}")
    finally:
        print("End drop_column")
        return df
