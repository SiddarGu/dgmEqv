
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {'Date': ['2019-04-25', '2019-04-26', '2019-04-27', '2019-04-28', '2019-04-29', '2019-04-30', '2019-05-01'],
        'Open Price ($)': [50.5, 52, 51.5, 54, 55.2, 56.6, 57.8],
        'Close Price ($)': [53, 51.9, 54, 55.2, 57.2, 58.1, 56.9],
        'High Price ($)': [54.2, 55.2, 55.7, 56.6, 58.2, 59.3, 59.2],
        'Low Price ($)': [49.8, 49.7, 50.8, 52.3, 54.6, 55.7, 55.2]
        }

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

df.rename(columns={'Open Price ($)': 'Open', 
                   'High Price ($)': 'High',
                   'Low Price ($)': 'Low',
                   'Close Price ($)': 'Close'}, inplace=True)

mpf.plot(df, type='candle', figratio=(12, 6), title='Sports and Entertainment Company Stock Performance - Weekly Overview',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/2_202312252258.png'))