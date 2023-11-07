import pandas as pd
from sqlalchemy import create_engine


def load_dataframe_to_database(df):
    is_successful = True
    try:
        # Map dataframe columns to database columns
        df_mapped = df.rename(
            columns={
                "Date": "date",
                "Symbol": "symbol",
                "Open": "open",
                "High": "high",
                "Low": "low",
                "Adj Close": "adj_close",
                "Volume": "volume",
                "Basic EPS": "basic_eps",
                "Net Income": "net_income",
                "Total Revenue": "total_revenue",
                "Total Expenses": "total_expenses",
                "Total Debt": "total_debt",
                "Total Capitalization": "total_capitalization",
                "Total Assets": "total_assets",
                "Free Cash Flow": "free_cash_flow",
                "Capital Expenditure": "capital_expenditure",
                "Close": "close",
            }
        )
        # Create a SQLite database engine
        engine = create_engine("sqlite:///sp500_db.db")
        table_name = "sp500"
        # Save the DataFrame to the SQLite table
        df_mapped.to_sql(table_name, con=engine, index=False, if_exists="replace")
    except Exception as e:
        is_successful = False
        print(f"Error occured while loading dataframe into database: {e}")
    finally:
        return is_successful
