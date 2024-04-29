
import mplfinance as mpf
import matplotlib.pyplot as plt
import pandas as pd

data = [['2020-07-01', 100.5, 105.7, 107.8, 99.2], 
        ['2020-07-02', 106.5, 107.4, 109.2, 104.9], 
        ['2020-07-03', 107.4, 109.1, 110.3, 106.2], 
        ['2020-07-04', 109.3, 108.4, 110.4, 106.9], 
        ['2020-07-05', 108.5, 106.2, 109.2, 104.5], 
        ['2020-07-06', 105.9, 107.1, 108.2, 103.6], 
        ['2020-07-07', 106.9, 105.2, 107.8, 102.7], 
        ['2020-07-08', 104.3, 103.7, 106.1, 102.2]]

df = pd.DataFrame(data, columns=['Date', 'Opening Price ($)', 'Closing Price ($)', 'High Price ($)', 'Low Price ($)'])
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.rename(columns={'Opening Price ($)': 'Open', 'Closing Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

mpf.plot(df, type='candle', figratio=(12,6), title='Finance Trend in Government and Public Policy - Weekly Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/24_202312270050.png'))