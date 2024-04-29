import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Create the DataFrame
data = {'Date': ['2021-01-04', '2021-01-11', '2021-01-18', '2021-05-25',
                 '2021-06-01', '2021-06-08', '2021-06-15', '2021-06-22',
                 '2021-06-29', '2021-12-07'],
        'Open Price ($)': [180, 185, 190, 195, 200, 205, 210, 215, 220, 225],
        'Close Price ($)': [185, 190, 195, 200, 205, 210, 215, 220, 225, 230],
        'High Price ($)': [190, 195, 200, 205, 210, 215, 220, 225, 230, 235],
        'Low Price ($)': [175, 180, 185, 190, 195, 200, 205, 210, 215, 220]}
df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns to match mplfinance column requirements
df.rename(columns={'Open Price ($)': 'Open',
                   'Close Price ($)': 'Close',
                   'High Price ($)': 'High',
                   'Low Price ($)': 'Low'}, inplace=True)

# Create the candlestick chart
mpf.plot(df, type='candle', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/125_202312302321.png'), figratio=(12,6),
         title='Social Media Company\'s Weekly Stock Performance in 2021')
