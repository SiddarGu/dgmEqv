
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance

data = [['2020-07-01', 125, 127.2, 134.5, 119], 
        ['2020-07-08', 129, 127.6, 133.2, 118.2], 
        ['2020-07-15', 134, 137.5, 140, 125.3], 
        ['2020-08-05', 127, 125.5, 134.2, 121.5],
        ['2020-08-12', 135, 134.2, 139.3, 128.3]]
df = pd.DataFrame(data, columns=['Month', 'Open Price (USD)', 'Close Price (USD)', 'High Price (USD)', 'Low Price (USD)'])

df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)
df.rename(columns = {'Open Price (USD)': 'Open', 'Close Price (USD)': 'Close', 'High Price (USD)': 'High', 'Low Price (USD)': 'Low'}, inplace=True)

mplfinance.plot(df, type='candle', figratio=(12,6), title='Science and Engineering Investment Trend - Monthly Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/10_202312270050.png'))