import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Define the data
data = {
    'Date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01'],
    'Open Price ($)': [120.00, 122.00, 124.00, 126.00, 128.00, 130.00, 132.00],
    'Close Price ($)': [122.50, 124.50, 126.50, 128.50, 130.50, 132.50, 134.50],
    'High Price ($)': [125.00, 127.00, 129.00, 131.00, 133.00, 135.00, 137.00],
    'Low Price ($)': [117.50, 119.50, 121.50, 123.50, 125.50, 127.50, 129.50]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns to match mplfinance requirements
df.rename(columns={
    'Open Price ($)': 'Open',
    'Close Price ($)': 'Close',
    'High Price ($)': 'High',
    'Low Price ($)': 'Low'
}, inplace=True)

# Create a figure
fig = plt.figure(figsize=(12, 6))

# Create the candlestick chart
mpf.plot(df, type='candle', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/93_202312302321.png'), title='Green Energy Stocks Monthly Trend Analysis')