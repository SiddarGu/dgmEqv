
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

# create dataframe
df = pd.DataFrame({'Date':['2019-05-06','2019-05-13','2019-05-20','2019-05-27','2019-06-03','2019-06-10','2019-06-17','2019-06-24'], 
                   'Opening Price ($)':[56.2,59.4,63.3,61.3,58.2,59.8,60.7,54.3],
                  'Closing Price ($)':[59.3,61.2,61.5,62.2,60.7,60.3,58.3,56.2],
                  'High Price ($)':[60.5,62.4,64.2,63.8,62.5,61.2,61.1,57.3],
                  'Low Price ($)':[54.2,55.1,58.9,59.8,56.4,59.2,56.4,53.0]
                  })

# convert date to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# rename columns
df = df.rename(columns={'Opening Price ($)':'Open','Closing Price ($)':'Close','High Price ($)':'High','Low Price ($)':'Low'})

# create the candlestick chart
plt.figure(figsize=(20,10))
mpf.plot(df, type='candle', volume=False, title='Financial Trend of Retail and E-commerce Market', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/8_202312270050.png'))