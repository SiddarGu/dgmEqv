import pandas as pd
import mplfinance as mpf

# Input data
data = [["2022-01-15", 1800, 1850, 1900, 1750],
        ["2022-01-22", 1850, 1890, 1950, 1800],
        ["2022-01-29", 1890, 1930, 1980, 1850],
        ["2022-02-05", 1930, 1980, 2030, 1900],
        ["2022-02-12", 1980, 2030, 2080, 1950],
        ["2022-02-19", 2030, 2080, 2130, 2000],
        ["2022-02-26", 2080, 2020, 2100, 2000]]

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Date", "Open", "Close", "High", "Low"])

# Convert 'Date' to datetime and set as index
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

# Rename columns to match mplfinance column requirements
df.rename(columns={"Open": "open", "High": "high", "Low": "low", "Close": "close"}, inplace=True)

# Create figure and plot candlestick chart
mpf.plot(df, type="candle", style="yahoo", figratio=(12,6), title="Weekly Hotel Stocks Value Trend in the Tourism and Hospitality Industry",
         ylabel="Stock Price ($)", savefig=dict(fname="/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/95_202312302321.png"))
