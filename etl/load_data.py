import pandas as pd
import sqlite3
from sqlalchemy import create_engine


def load_dataframe_to_database(df):
    is_successful = True
    try:
        print("Start load_dataframe_to_database")
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

        # connection = sqlite3.connect("../database/data/sp500_db")
        # # run query
        # cursor = connection.cursor()
        # sql = f"""INSERT INTO sp500 (date, symbol, open, high, low, adj_close, volume, basic_eps, net_income, total_revenue, total_expenses, total_debt, total_capitalization, total_assets, free_cash_flow, capital_expenditure, close) VALUES ()"""
        # cursor.execute(sql)
        # connection.commit()

        # Create a SQLite database engine
        database_path = "../database/data/sp500_db"
        engine = create_engine(f"sqlite:///{database_path}")
        table_name = "sp500"
        # Save the DataFrame to the SQLite table
        df_mapped.to_sql(table_name, con=engine, index=False, if_exists="append")
    except Exception as e:
        is_successful = False
        print(f"Error occured while loading dataframe into database: {e}")
    finally:
        print("End load_dataframe_to_database")
        return is_successful
