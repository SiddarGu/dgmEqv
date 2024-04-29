import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Define the data
data = {'Date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01', '2021-07-01', '2021-08-01'],
        'Opening Price ($)': [100.5, 102, 105, 106, 108, 110, 112, 114],
        'Closing Price ($)': [102, 103.1, 104, 108.7, 110.9, 112.9, 114.9, 116.9],
        'High Price ($)': [104.2, 105.2, 105, 109.6, 111.2, 113.2, 115.2, 117.2],
        'Low Price ($)': [98.8, 100.9, 102.7, 105.4, 107, 108, 110, 112]}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as index
df.set_index('Date', inplace=True)

# Rename columns
df.rename(columns={'Opening Price ($)': 'Open',
                   'Closing Price ($)': 'Close',
                   'High Price ($)': 'High',
                   'Low Price ($)': 'Low'}, inplace=True)

# Create a candlestick chart
mpf.plot(df, type='candle', figratio=(12, 6), title='Academic Publishing Industry Stock Trend Overview',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/96_202312302321.png'))