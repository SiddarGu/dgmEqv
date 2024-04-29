import pandas as pd
import mplfinance as mpf

# Create DataFrame
data = {'Date': ['2018-01-01', '2018-01-08', '2018-01-15', '2018-01-22', '2018-01-29'],
        'Open Price ($)': [1200, 1280, 1300, 1330, 1350],
        'Close Price ($)': [1250, 1300, 1320, 1350, 1400],
        'High Price ($)': [1300, 1350, 1400, 1400, 1450],
        'Low Price ($)': [1100, 1200, 1280, 1300, 1330]}

df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns
df.rename(columns={'Open Price ($)': 'Open',
                   'Close Price ($)': 'Close',
                   'High Price ($)': 'High',
                   'Low Price ($)': 'Low'}, inplace=True)

# Create candlestick chart
mpf.plot(df, type='candle', figratio=(12, 6), title='Weekly Price Range of Artwork Auctions', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/74_202312302321.png'))
