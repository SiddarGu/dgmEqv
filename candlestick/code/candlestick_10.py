
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

df = pd.DataFrame({'Date': ['2019-05-17', '2019-05-24', '2019-05-31', '2019-06-07', '2019-06-14', '2019-06-21', '2019-06-28'], 
                   'Opening Price ($)' : [30, 31, 33, 34, 30, 31, 33],
                   'Closing Price ($)' : [32, 34, 35, 36, 32, 34, 35],
                   'High Price ($)' : [34, 35, 37, 38, 34, 36, 37],
                   'Low Price ($)' : [28, 29, 31, 32, 28, 29, 31]})
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.rename({'Opening Price ($)': 'Open',
           'Closing Price ($)': 'Close',
           'High Price ($)': 'High',
           'Low Price ($)': 'Low'}, axis=1, inplace=True)

mpf.plot(df, type='candle', figratio=(12,6), title='Arts and Culture Industry Stock Performance - Week Overview', 
          savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/8_202312252310.png'))