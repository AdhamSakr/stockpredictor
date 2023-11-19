from pymongo import MongoClient


def load_dataframe_to_database(df):
    is_successful = True
    try:
        print("Start load_dataframe_to_database")
        connection_string = "mongodb+srv://AdhamSakr:EDsxIryI4nhgtAHc@cluster0.mdltzjn.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(connection_string)
        db = client.sp500_db
        collection = db.sp500

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

        # Convert DataFrame to a list of dictionaries
        data_dict = df_mapped.to_dict(orient="records")

        # Insert documents into the MongoDB collection
        collection.insert_many(data_dict)
    except Exception as e:
        is_successful = False
        print(f"Error occured while loading dataframe into database: {e}")
    finally:
        print("End load_dataframe_to_database")
        return is_successful
