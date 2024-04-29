
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = [['2020-08',75.2,80.6,81.2,73.5],
        ['2020-09',81.7,78.2,84.3,76.4],
        ['2020-10',79.6,77.2,81.4,75.3],
        ['2020-11',77.8,80.5,83.1,76.3],
        ['2020-12',80.7,78.4,83.1,75.9]]

df = pd.DataFrame(data, columns=['Month','Open Price ($)','Close Price ($)','High Price ($)','Low Price ($)'])
df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True) 
df = df.rename(columns={'Open Price ($)':'Open','Close Price ($)':'Close','High Price ($)':'High','Low Price ($)':'Low'})

mpf.plot(df, type='candle', figratio=(12,6), title='Financial Performance of Sports and Entertainment Stocks - Monthly Overview',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/4_202312270050.png'))