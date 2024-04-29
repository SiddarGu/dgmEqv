import pandas as pd
import mplfinance as mpf

# Define the data
data = {
    'Date': ['2020-05-01', '2020-05-02', '2020-05-03', '2020-05-04', '2020-05-05', '2020-05-06', '2020-05-07', '2020-05-08', '2020-05-09', '2020-05-10', '2020-05-11'],
    'Open Price ($)': [70, 72, 75, 73, 78, 82, 85, 90, 92, 96, 98],
    'Close Price ($)': [72, 74, 73, 76, 80, 85, 88, 92, 94, 98, 100],
    'High Price ($)': [73, 75, 76, 78, 82, 87, 90, 94, 96, 100, 102],
    'Low Price ($)': [67, 70, 71, 71, 76, 80, 82, 85, 88, 92, 94]
}

# Create a DataFrame
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

# Create a figure and save as candlestick chart
fig = mpf.plot(df, type='candle', figratio=(12,6), savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/71_202312302321.png'),
               style='yahoo', title='Book Publishing Company Stock Trend Analysis in May 2020')
