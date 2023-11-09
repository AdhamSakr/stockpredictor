import datetime
from extract_data import (
    extract_technical_data,
    extract_historical_fundamental_data,
    extract_yesterdays_fundamental_data,
)
from transform_data import (
    merge_technical_fundamental_data,
    set_date_as_index,
    change_column_datatypes,
    drop_null_values,
)
from load_data import load_dataframe_to_database


if __name__ == "__main__":
    date_today = str(datetime.date.today())
    date_from_2_years = str(datetime.date.today() - datetime.timedelta(days=2 * 365))
    date_yesterday = str(datetime.date.today() - datetime.timedelta(days=1))

    # Extract historical data
    technical_df = extract_technical_data(date_from_2_years, date_today)
    fundamental_df = extract_historical_fundamental_data(date_from_2_years, date_today)

    # Extract yesterday's data
    # techincal_df = extract_technical_data(date_yesterday, date_today)
    # fundamental_df = extract_yesterdays_fundamental_data(date_yesterday)

    # Transform data
    sp500_df = merge_technical_fundamental_data(technical_df, fundamental_df)
    sp500_df = set_date_as_index(sp500_df)
    sp500_df = change_column_datatypes(sp500_df)
    sp500_df = drop_null_values(sp500_df)

    # Load data to database
    load_dataframe_to_database(sp500_df)
