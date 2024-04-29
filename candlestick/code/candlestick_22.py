
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

data=[[pd.to_datetime('2021-01-15'),30.2,34.7,37.8,27.1], 
      [pd.to_datetime('2021-01-22'),34.2,38.1,41.4,32.7], 
      [pd.to_datetime('2021-02-05'),40,42.3,45.5,36.2],
      [pd.to_datetime('2021-02-12'),45.5,43.7,48,39.5],
      [pd.to_datetime('2021-02-19'),43.8,41,45.7,37.9],
      [pd.to_datetime('2021-02-26'),40.5,42.8,45.4,37.9]]

df = pd.DataFrame(data, columns=['Date','Open','Close','High','Low'])
df.set_index('Date', inplace=True)
df.rename(columns={'Open':'Open','Close':'Close','High':'High','Low':'Low'}, inplace=True)

fig = plt.figure(figsize=(10,7))
mpf.plot(df, type='candle', title='Energy and Utilities Market Overview', 
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/14_202312252310.png'))