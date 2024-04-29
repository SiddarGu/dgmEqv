import pandas as pd
import mplfinance as mpf

# Input data
data = {'Date': ['2021-01-04', '2021-01-11', '2021-01-18', '2021-01-25', '2021-02-01', '2021-02-08', '2021-02-15', '2021-02-22'],
        'Open Price ($)': [100, 110, 108, 115, 118, 123, 132, 138],
        'Close Price ($)': [105.2, 108.5, 110.6, 116, 123.4, 132.5, 135, 133.7],
        'High Price ($)': [108, 112.6, 114, 120, 125.2, 135.6, 140.2, 142.6],
        'Low Price ($)': [95.5, 106, 105.2, 112.3, 116.6, 122, 129.7, 131.2]}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns to match mplfinance column requirements
df.rename(columns={'Open Price ($)': 'Open', 'Close Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

# Create candlestick chart
mpf.plot(df, type='candle', title='Social Media Company Stock Performance - Quarter 1 Overview', figratio=(12, 6), savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/107_202312302321.png'))
