
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

data = [['2019-10-14', 45.2, 47.1, 48.2, 44],
        ['2019-10-21', 45.5, 46.3, 49.1, 43.2],
        ['2019-10-28', 47.4, 43.6, 48.2, 42.8],
        ['2019-11-04', 45.7, 48.2, 50.1, 43],
        ['2019-11-11', 47.1, 46.7, 48.5, 45.2],
        ['2019-11-18', 48.3, 47.4, 49.5, 45.5],
        ['2019-11-25', 48.5, 46.2, 49.4, 44.9]]

df = pd.DataFrame(data, columns=['Date', 'Open', 'Close', 'High', 'Low'])
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

mpf.plot(df, type='candle', figratio=(12, 6), title='Financial Trends of Food and Beverage Industry Over One Month', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/1_202312270050.png'))