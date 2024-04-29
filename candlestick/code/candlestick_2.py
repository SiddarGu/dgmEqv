
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

data=[('2019-04-21',10.5,12.2,14.1,9.1),('2019-04-22',14.3,12.2,14.8,10.4),('2019-04-23',11.3,13.7,15.8,10.2),('2019-04-24',15.6,14.2,16.4,12.3),('2019-04-25',13.5,14.7,16.2,11.8),('2019-04-26',14.2,15.8,17.3,13.1),('2019-04-27',15.5,14.1,16.2,12.8),('2019-04-28',14.7,15.2,16.3,13.4)]

df=pd.DataFrame(data, columns=['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])
df['Date']=pd.to_datetime(df['Date'])
df=df.set_index('Date')
df.rename(columns={'Opening Price ($)':'Open','Closing Price ($)':'Close','High Price ($)':'High','Low Price ($)':'Low'}, inplace=True)

mpf.plot(df, type='candle', figratio=(12,6),title='Healthcare and Health Stock Price Fluctuation - Weekly Overview',savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/23_202312270050.png'))