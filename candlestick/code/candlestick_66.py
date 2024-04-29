import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# Create DataFrame with the given data
data = {'Date': ['2021-01-06', '2021-01-13', '2021-01-20', '2021-01-27', '2021-02-03', '2021-02-10', '2021-02-17', '2021-02-24', '2021-03-03', '2021-03-10'],
        'Opening Price ($)': [35, 38, 37, 41, 45, 44, 50, 47, 48, 53],
        'Closing Price ($)': [37.5, 36.9, 39.5, 42.7, 46.3, 48.9, 48.5, 45.5, 52, 54],
        'High Price ($)': [38, 39, 41, 45, 47.7, 49.7, 51, 49, 53, 55],
        'Low Price ($)': [33, 34, 36, 39.5, 42.5, 43, 46, 43, 46.7, 48.5]}

df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns to match mplfinance column requirements
df.rename(columns={'Opening Price ($)': 'Open', 'Closing Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

# Create candlestick chart using mplfinance
mpf.plot(df, type='candle', figratio=(8, 6), style='yahoo', title='Financial Trend in Music and Performing Arts Sector', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/119_202312302321.png'))
