import pandas as pd
import mplfinance as mpf

data = {'Date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01', '2020-10-01', '2020-11-01', '2020-12-01'],
        'Open Price ($)': [120, 130, 110, 100, 90, 105, 90, 85, 100, 110, 105, 115],
        'Close Price ($)': [125, 140, 125, 110, 105, 110, 95, 90, 105, 115, 110, 120],
        'High Price ($)': [130, 145, 135, 115, 110, 115, 100, 95, 110, 120, 115, 125],
        'Low Price ($)': [115, 120, 105, 95, 85, 100, 85, 80, 95, 105, 100, 110]}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df = df.rename(columns={'Open Price ($)': 'Open', 'Close Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'})

fig = mpf.plot(df, type='candle', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/29_202312302321.png'), title='Annual Art Auction Pricing Trend in 2020', figratio=(12,6))