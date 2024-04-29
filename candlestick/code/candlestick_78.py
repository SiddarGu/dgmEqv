import pandas as pd
import mplfinance as mpf

# Define the data
data = {
    'Date': ['2021-04-01', '2021-04-02', '2021-04-03', '2021-04-04', '2021-04-05', '2021-04-06', '2021-04-07', '2021-04-08', '2021-04-09', '2021-04-10', '2021-04-11'],
    'Opening Price ($)': [105.6, 108.7, 111.4, 110, 113.5, 116, 118.5, 121, 123.5, 126, 125],
    'Closing Price ($)': [108.3, 110.5, 109.7, 112.5, 115.3, 118, 120, 122.5, 125.5, 124, 126.5],
    'High Price ($)': [109.2, 112.4, 113.2, 115, 116.6, 121, 124, 127, 130, 131.5, 134],
    'Low Price ($)': [104, 107.4, 108, 109, 110, 114, 115, 119, 120, 121, 122]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# Rename columns to match mplfinance column requirements
df = df.rename(columns={
    'Opening Price ($)': 'Open',
    'Closing Price ($)': 'Close',
    'High Price ($)': 'High',
    'Low Price ($)': 'Low'
})

# Create a figure and save as a candlestick chart
fig = mpf.plot(df, type='candle', figratio=(12, 6), style='classic', title='Manufacturing and Production Sector Stock Trends', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/67_202312302321.png'))