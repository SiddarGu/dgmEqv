import pandas as pd
import mplfinance as mpf

data = {'Date': ['2021-05-01', '2021-05-08', '2021-05-15', '2021-05-22', '2021-05-29', '2021-06-05'],
        'Open Price ($)': [150, 154, 154.8, 158.5, 159.3, 161.7],
        'Close Price ($)': [152.4, 156.1, 157.5, 160.6, 161, 160],
        'High Price ($)': [154.8, 158.7, 160.1, 161.9, 162.3, 164.9],
        'Low Price ($)': [145, 151.2, 148.3, 149.2, 150.3, 152.3]}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.rename(columns={'Open Price ($)': 'Open', 'Close Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

fig = mpf.figure()
mpf.plot(df, type='candle', show_nontrading=False, style='yahoo', title='Weekly performance of Transportation and Logistic Stocks',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/55_202312302321.png'),
         figratio=(12, 9))
