
import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt

data = [['2019-04-01',50.2,51.5,53.2,48.2],
['2019-04-08',51.3,54.2,56.0,50.5],
['2019-04-15',54.9,55.4,56.8,53.7],
['2019-04-22',55.0,56.5,57.2,53.8],
['2019-04-29',56.2,54.9,58.1,52.9]]

df = pd.DataFrame(data, columns=['Date','Open','Close','High','Low'])
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

mpf.plot(df, figratio=(12,6), title='Manufacturing and Production Company Stock Performance - Week Overview',savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/Full/candlestick/png_val/candlestick_16.png'))