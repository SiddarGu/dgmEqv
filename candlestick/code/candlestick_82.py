
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

df = pd.DataFrame([['2019-05-04', 50.4, 52.2, 54.1, 48.3],
                   ['2019-05-11', 51.3, 52.7, 54.2, 50.7],
                   ['2019-05-18', 53.1, 54.7, 56.3, 51.6],
                   ['2019-06-01', 54.5, 55.9, 57.8, 53.2],
                   ['2019-06-08', 54.9, 57.2, 58.1, 53.8],
                   ['2019-06-15', 56.7, 58.3, 60.2, 54.3],
                   ['2019-06-22', 56.8, 59.5, 61.2, 54.9]],
                  columns=['Date','Opening Price ($)','Closing Price ($)','High Price ($)', 'Low Price ($)'])

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df = df.rename(columns={'Opening Price ($)': 'Open', 'Closing Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'})

mpf.plot(df, type='candle', figratio=(12,6), title='Trend of Retail and E-commerce Stock Prices - Monthly Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/25_202312270050.png'))