import sqlite3
import logging

if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.DEBUG)

        # connect to database
        connection = sqlite3.connect("sp500_db")
        logging.debug("Connected to database successfully")

        # drop any previous sp500 table
        sql_drop = """DROP TABLE IF EXISTS sp500"""

        # create sp500 table
        sql_create = """
        CREATE TABLE sp500 (
        date TEXT,
        symbol TEXT,
        open TEXT,
        high TEXT,
        low TEXT,
        adj_close TEXT,
        close TEXT,
        volume TEXT,
        basic_eps TEXT,
        net_income TEXT,
        total_revenue TEXT,
        total_expenses TEXT,
        total_debt TEXT,
        total_capitalization TEXT,
        total_assets TEXT,
        free_cash_flow TEXT,
        capital_expenditure TEXT,
        PRIMARY KEY (date, symbol)
        )"""

        # Remove sp500 table if it already exists
        connection.execute(sql_drop)
        logging.debug("sp500 table dropped successfully!")
        # Create sp500 table
        connection.execute(sql_create)
        logging.debug("sp500 table created successfully!")
        connection.close()
    except Exception as e:
        logging.debug(f"Error occured: {e}")
