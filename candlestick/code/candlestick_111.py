
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {'Date':['2019-06-03','2019-06-10','2019-06-17','2019-06-24','2019-07-01','2019-07-08','2019-07-15','2019-07-22'],
        'Opening Price ($)':[20.5,21.0,22.3,23.2,19.6,21.2,19.6,25.2],
        'Closing Price ($)':[22.9,22.7,23.5,21.7,20.8,20.1,21.4,24.2],
        'High Price ($)':[25.2,24.2,25.6,24.2,22.6,22.3,24.2,27.6],
        'Low Price ($)':[17.8,19.9,20.4,19.8,18.4,18.4,17.8,20.4]}

df = pd.DataFrame(data) 
df['Date']=pd.to_datetime(df['Date'])
df = df.set_index('Date')
df = df.rename(columns={'Opening Price ($)':'Open', 'Closing Price ($)':'Close', 'High Price ($)':'High', 'Low Price ($)':'Low'})

fig = plt.figure(figsize=(20,10))
mpf.plot(df,type='candle',title='Financial Trend of Government and Public Policy Sector',savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/5_202312252258.png'))