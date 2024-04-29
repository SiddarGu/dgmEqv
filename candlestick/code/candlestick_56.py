import pandas as pd
import mplfinance as mpf

data = {'Date': ['2022-01-03', '2022-01-10', '2022-01-17', '2022-01-24', '2022-01-31', '2022-02-07', '2022-02-14', '2022-02-21', '2022-02-28'],
        'Open Price ($)': [40, 41, 47, 48.5, 49, 51.5, 54, 55.5, 57],
        'Close Price ($)': [42, 46, 48, 49, 51, 53, 55, 57, 59],
        'High Price ($)': [43.5, 47, 50, 51, 52, 55, 57, 58, 61],
        'Low Price ($)': [39.5, 40.5, 46, 48, 48.5, 51, 53, 54, 56.5]}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

column_names = {'Open Price ($)': 'Open', 'Close Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'}
df = df.rename(columns=column_names)

fig = mpf.figure(figsize=(8, 6))

mc = mpf.make_marketcolors(up='g', down='r')
s = mpf.make_mpf_style(marketcolors=mc)

mpf.plot(df, type='candle', style=s, title='Weekly Trends of Legal Consultancy Firm Stocks', figratio=(12,6), savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/88_202312302321.png'))
