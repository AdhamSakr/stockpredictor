from yahoo_fin import stock_info


def extract_technical_data(stock_code, start_date, end_date):
    technical_data = stock_info.get_data(stock_code, start_date, end_date)
    return technical_data


def extract_fundamental_data(stock_code):
    fundamental_data = stock_info.get_quote_table(stock_code)
    return fundamental_data
