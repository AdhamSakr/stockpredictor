import pandas as pd
from yahoo_fin import stock_info
import yfinance as yf

# Fundamental data columns to be selected
selected_income_statement_columns = [
    "Basic EPS",
    "Net Income",
    "Total Revenue",
    "Total Expenses",
]
selected_balance_sheet_columns = ["Total Debt", "Total Capitalization", "Total Assets"]
selected_cash_flow_columns = ["Free Cash Flow", "Capital Expenditure"]


def extract_technical_data(start_date, end_date):
    sp500_stocks = get_sp500_list()
    technical_df = pd.DataFrame()
    for stock in sp500_stocks:
        try:
            stock_historical_data = yf.download(
                stock, start=start_date, end=end_date, progress=False
            )
            stock_historical_data["Symbol"] = stock
            technical_df = pd.concat([technical_df, stock_historical_data])
        except Exception as e:
            print(f"Error retrieving data for {stock}: {e}")

    try:
        # Convert "Date" from index to a normal column as it will have duplicates for different stocks
        technical_df.reset_index(inplace=True)
    except Exception as e:
        print("Error resetting index of technical dataframe")

    return technical_df


def extract_historical_fundamental_data(start_date, end_date):
    sp500_stocks = get_sp500_list()
    fundamental_df = pd.DataFrame()
    for stock in sp500_stocks:
        try:
            stock_ticker = yf.Ticker(stock)
            # Get quarterly income statement
            quarterly_income_statement = stock_ticker.quarterly_incomestmt.transpose()
            # Get quarterly balance sheet
            quarterly_balance_sheet = stock_ticker.quarterly_balance_sheet.transpose()
            # Get quarterly cash flow
            quarterly_cash_flow = stock_ticker.quarterly_cashflow.transpose()
            # Merge the different fundamental data sources
            stock_fundamental_data = pd.merge(
                quarterly_income_statement[selected_income_statement_columns],
                quarterly_balance_sheet[selected_balance_sheet_columns],
                left_index=True,
                right_index=True,
            )
            stock_fundamental_data = pd.merge(
                stock_fundamental_data,
                quarterly_cash_flow[selected_cash_flow_columns],
                left_index=True,
                right_index=True,
            )
            # Add a new column for the stock symbol
            stock_fundamental_data["Symbol"] = stock
            stock_fundamental_data = stock_fundamental_data.resample("D").ffill()
            stock_fundamental_data = stock_fundamental_data[
                (stock_fundamental_data.index >= start_date)
                & (stock_fundamental_data.index <= end_date)
            ]
            fundamental_df = pd.concat([fundamental_df, stock_fundamental_data])
        except Exception as e:
            print(f"Error retrieving data for {stock}: {e}")

    try:
        # Rename index to be "Date" then convert it to a normal column as it has duplicates
        fundamental_df.reset_index(inplace=True)
        fundamental_df.rename(columns={"index": "Date"}, inplace=True)
        fundamental_df["Date"] = pd.to_datetime(fundamental_df["Date"])
    except Exception as e:
        print("Error resetting index of historical fundamental dataframe")

    return fundamental_df


def extract_yesterdays_fundamental_data():
    sp500_stocks = get_sp500_list()
    yesterday_fundamental_df = pd.DataFrame()
    for stock in sp500_stocks:
        try:
            stock_ticker = yf.Ticker(stock)
            # Get quarterly income statement
            quarterly_income_statement = (
                stock_ticker.quarterly_incomestmt.transpose().head(1)
            )
            # Get quarterly balance sheet
            quarterly_balance_sheet = (
                stock_ticker.quarterly_balance_sheet.transpose().head(1)
            )
            # Get quarterly cash flow
            quarterly_cash_flow = stock_ticker.quarterly_cashflow.transpose().head(1)
            # Merge the different fundamental data sources
            data = pd.merge(
                quarterly_income_statement[selected_income_statement_columns],
                quarterly_balance_sheet[selected_balance_sheet_columns],
                left_index=True,
                right_index=True,
            )
            data = pd.merge(
                data,
                quarterly_cash_flow[selected_cash_flow_columns],
                left_index=True,
                right_index=True,
            )
            # Add new columns for the stock symbol and date of yesterday
            data["Symbol"] = stock
            data["Date"] = date_yesterday
            # Concat to the final dataframe
            yesterday_fundamental_df = pd.concat([yesterday_fundamental_df, data])
        except Exception as e:
            print(f"Error retrieving data for {stock}: {e}")

    try:
        # Remove old Date index as it will be replaced with yesterday's date through the loop
        yesterday_fundamental_df.reset_index(inplace=True, drop=True)
    except Exception as e:
        print("Error resetting index of yesterday's fundamental dataframe")

    return yesterday_fundamental_df


def get_sp500_list():
    sp500_stocks = pd.read_html(
        "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    )[0]["Symbol"].tolist()

    return sp500_stocks
