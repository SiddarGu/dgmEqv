
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

df = pd.DataFrame({'Date':['2019-05-11','2019-05-12','2019-05-13','2019-05-14','2019-05-15','2019-05-16','2019-05-17'],'Open Price ($)':[50,50.3,51.2,50.8,51.5,50.9,51.1],'Close Price ($)':[49.2,51,51.3,51.2,50.3,51.7,50.4],'High Price ($)':[51.9,53.3,53.5,52.5,53,53.2,51.8],'Low Price ($)':[48.7,49.4,50.2,50.4,48.9,50.4,49.2]})
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df=df.rename(columns={'Open Price ($)':'Open','Close Price ($)':'Close','High Price ($)':'High','Low Price ($)':'Low'})

plt.figure(figsize=(30,20))
mpf.plot(df, type='candle', figratio=(12, 6), title='Financial Performance of Charity and Nonprofit Organizations - Weekly Overview',savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/1_202312252310.png'))