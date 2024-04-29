
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

data = [['2019-05-15',60,65,70,58],['2019-05-16',67,62,68,56],['2019-05-17',65,63,68,60],['2019-05-18',62,60,63,58],['2019-05-19',61,63,67,59],['2019-05-20',65,68,69,62]]
df = pd.DataFrame(data,columns=['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)
df.rename(columns={'Opening Price ($)':'Open','Closing Price ($)':'Close','High Price ($)':'High','Low Price ($)':'Low'},inplace=True)

mpf.plot(df, figratio=(12,6),savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/19_202312252310.png'),title="Social Media and Web-based Stock Performance - Five Day Overview")