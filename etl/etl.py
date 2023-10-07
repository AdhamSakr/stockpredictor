from extract_data import extract_technical_data, extract_fundamental_data
from transform_data import transform_technical_data, transform_fundamental_data
from load_data import load_data_to_database

# Example stock symbol and date range
symbol = "AAPL"
start_date = "2022-01-01"
end_date = "2023-01-01"

# Extract data
stock_data = extract_technical_data(symbol, start_date, end_date)
fundamental_data = extract_fundamental_data(symbol)

# Transform data
transformed_stock_data = transform_technical_data(stock_data)
transformed_fundamental_data = transform_fundamental_data(fundamental_data)

# Load data to database
load_data_to_database(transformed_stock_data, "stock_data.csv")
