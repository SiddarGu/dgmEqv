
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

data = [['2020-08-01', 43, 44.2, 45.9, 41.5],
        ['2020-08-08', 45.3, 43.2, 46.6, 42.1],
        ['2020-08-15', 40.9, 41.9, 44.2, 38.7],
        ['2020-08-22', 43.2, 43.6, 44.7, 40.4],
        ['2020-09-05', 44, 45.8, 47.1, 41.9],
        ['2020-09-12', 44.5, 45, 46.3, 43.1],
        ['2020-09-19', 43.2, 45.9, 47.5, 41.5]]

df = pd.DataFrame(data, columns=['Date', 'Open', 'Close', 'High', 'Low'])
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

mpf.plot(df, type='candle', figratio=(12, 6), title='Financial Performance of Charity and Nonprofit Organizations - Weekly Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/3_202312252310.png'))