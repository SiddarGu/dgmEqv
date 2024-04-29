
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {'Date': ['2020-07-01', '2020-07-08', '2020-07-15', '2020-07-22', '2020-07-29', '2020-08-05', '2020-08-12', '2020-08-19'],
        'Opening Price ($)': [21, 24, 30, 30, 31, 36, 29, 24],
        'Closing Price ($)': [25, 27, 27, 34, 33, 32, 27, 22],
        'High Price ($)': [27, 30, 32, 37, 36, 38, 30, 25],
        'Low Price ($)': [19, 22, 25, 27, 29, 30, 25, 20]}

df = pd.DataFrame(data)
df.Date = pd.to_datetime(df.Date)
df = df.set_index('Date')
df = df.rename(columns={'Opening Price ($)': 'Open', 'Closing Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'})

mpf.plot(df, type='candle', figratio=(12,6), title='Financial Performance of Sports and Entertainment Company - Weekly Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/24_202312252310.png'))