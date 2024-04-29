import pandas as pd
import mplfinance as mpf

# Define the data
data = {'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', 
                 '2022-01-06', '2022-01-07', '2022-01-08', '2022-01-09', '2022-01-10'],
        'Open Price ($)': [103, 104, 107, 105, 109, 107, 110, 112, 115, 117],
        'Close Price ($)': [105.2, 106.8, 106, 108.7, 107, 109.5, 112.4, 114.6, 117, 119],
        'High Price ($)': [106, 108, 108, 109.9, 109.2, 111.9, 113.9, 115.8, 118.5, 121],
        'Low Price ($)': [101.3, 102.9, 103.2, 104.2, 105.3, 106.2, 108, 110.5, 113.8, 115]}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns to match mplfinance column requirements
df.rename(columns={'Open Price ($)': 'Open', 'Close Price ($)': 'Close',
                   'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

# Create the figure and plot the candlestick chart
fig = mpf.plot(df, type='candle', title='Transportation and Logistics Company Stock Prices in the First ten Days of 2022',
               figratio=(12,6),
               savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/76_202312302321.png'))