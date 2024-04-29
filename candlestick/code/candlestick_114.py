import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Define the data
data = {'Date': ['2022-03-01', '2022-03-02', '2022-03-03', '2022-03-04', '2022-03-05', '2022-03-06', '2022-03-07', '2022-03-08', '2022-03-09', '2022-03-10'],
        'Open Price ($)': [80, 85, 82, 90, 75, 78, 74, 82, 87, 86],
        'Close Price ($)': [85, 82, 89, 88, 78, 80, 78, 88, 85, 90],
        'High Price ($)': [90, 91, 93, 95, 80, 85, 80, 92, 89, 92],
        'Low Price ($)': [75, 80, 80, 85, 70, 73, 70, 80, 83, 83]}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns
df.rename(columns={'Open Price ($)': 'Open', 'Close Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

# Create candlestick chart
mpf.plot(df, type='candle', style='yahoo', figratio=(12,6), title='Transportation and Logistics Sector Stock Price Fluctuations in March 2022', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/90_202312302321.png'))