import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {'Date': ['2016-03-12', '2016-03-19', '2016-03-26', '2016-04-02', '2016-04-09', '2016-04-16', '2016-04-23', '2016-04-30'],
        'Opening Price ($)': [75.4, 78.2, 78.5, 80.7, 82.8, 85.5, 90, 92],
        'Closing Price ($)': [77.8, 77, 81, 83.8, 83.2, 88.9, 92, 95],
        'High Price ($)': [80.5, 82.5, 85.3, 86.2, 88.6, 91.2, 96.5, 98.5],
        'Low Price ($)': [72, 73.2, 75.7, 78.6, 80.5, 83, 85.7, 90]}

df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns to match mplfinance column requirements
df = df.rename(columns={'Opening Price ($)': 'Open', 'Closing Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'})

# Create a figure
fig = plt.figure()

# Create a candlestick chart
mpf.plot(df, type='candle', style='charles', title='Weekly Performance of Sustainable Energy Investment Fund', figratio=(12,6), savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/108_202312302321.png'))
