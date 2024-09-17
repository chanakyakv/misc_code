# from nsepython import *
# logging.basicConfig(level=logging.INFO)

# symbol = "SBIN"
# series = "EQ"
# start_date = "08-01-2021"
# end_date ="14-06-2021"
# print(equity_history(symbol,series,start_date,end_date))


from nsepython import *
import pandas as pd

def get_daily_volatility(symbol, series, start_date, end_date):
    # Fetch historical stock prices
    historical_data = equity_history(symbol, series, start_date, end_date)
    df = pd.DataFrame(historical_data) 
    df = df.drop('CA', axis=1)
    df = df.drop('_id', axis=1)
    df = df.drop_duplicates()
    df = df.sort_values('CH_TIMESTAMP')

    # Calculate daily returns
    df["pct_change"] = df['CH_CLOSING_PRICE'].pct_change().dropna()
    print(df["pct_change"].describe())

    df.to_csv("test.csv")
    print(df.head())

    # Calculate daily volatility (standard deviation of daily returns)
    daily_volatility = df["pct_change"].std()
    annual_voltality = daily_volatility * math.sqrt(len(df["pct_change"].index))


    return daily_volatility, annual_voltality

# Usage:
symbol = "SBIN"
series = "EQ"
start_date = "18-09-2023"
end_date = "17-09-2024"

daily_volatility = get_daily_volatility(symbol, series, start_date, end_date)

print(f'Daily Volatility: {daily_volatility}')
