
import pandas as pd 
import matplotlib.pyplot as plt 
import mplfinance as mpf

df = pd.DataFrame({'Month': ['August 2020', 'September 2020', 'October 2020', 'November 2020', 'December 2020'],
                   'Open Price ($)': [65, 73, 77, 75, 79],
                   'Close Price ($)': [70, 74, 74, 77, 80],
                   'High Price ($)': [72, 76, 79, 81, 82],
                   'Low Price ($)':  [60, 68, 71, 72, 76]})

df['Month'] = pd.to_datetime(df['Month'])
df = df.set_index('Month')
df = df.rename(columns={'Open Price ($)': 'Open', 'Close Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'})

mpf.plot(df, type='candle', figratio=(12,6), savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/5_202312252310.png'), title='Sports and Entertainment Stock Performance - Monthly Overview')