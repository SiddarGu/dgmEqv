
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data  = [['2020-10-15', 98.4, 95.7, 99.8, 94.3],
         ['2020-10-16', 94.8, 93.3, 96.6, 91.7],
         ['2020-10-17', 95.5, 96.6, 98.2, 93.1],
         ['2020-10-18', 97.7, 95.2, 98.5, 93.9],
         ['2020-10-19', 95.8, 96.4, 97.9, 94.6],
         ['2020-10-20', 96.7, 95.7, 97.9, 94.4]]

df = pd.DataFrame(data, columns=['Date', 'Open', 'Close', 'High', 'Low'])
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.rename(columns={'Open': 'Open', 'Close': 'Close', 'High': 'High', 'Low': 'Low'}, inplace=True)

fig = plt.figure(figsize=(18, 10))
mpf.plot(df, type='candle', title='Healthcare and Health Stock Price Performance Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/18_202312252310.png'))