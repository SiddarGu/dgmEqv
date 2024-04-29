
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = [['2019-05-01', 46.5, 48.9, 50.7, 44.2], 
        ['2019-05-02', 48.8, 46.7, 50.2, 44.3],
        ['2019-05-03', 47.5, 45.2, 48.9, 43.7],
        ['2019-05-04', 44.9, 47.6, 49.2, 43.4],
        ['2019-05-05', 46.1, 48.2, 49.5, 45.3],
        ['2019-05-06', 46.7, 48.5, 50.2, 44.2],
        ['2019-05-07', 49.3, 48.9, 50.1, 47.5]]

df = pd.DataFrame(data, columns=['Date', 'Open', 'Close', 'High', 'Low'])
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

mpf.plot(df, type='candle', title='Financial Trend of Technology and the Internet - Weekly Overview', figscale=3, figsize=(9, 6), savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/16_202312270050.png'))