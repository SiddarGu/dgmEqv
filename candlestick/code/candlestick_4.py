
import mplfinance as mpf
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(data=[['2019-04-26',2.1,2.2,2.5,1.8],
                        ['2019-04-27',2.3,2.2,2.6,2.1],
                        ['2019-04-28',2.3,2.3,2.5,2.0],
                        ['2019-04-29',2.4,2.5,2.7,2.2],
                        ['2019-04-30',2.5,2.7,2.8,2.4]],
                   columns=['Date','Open Price ($)','Close Price ($)','High Price ($)','Low Price ($)']
                  )

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.rename(columns={'Open Price ($)': 'Open', 
                   'Close Price ($)': 'Close',
                   'High Price ($)': 'High',
                   'Low Price ($)': 'Low'}, inplace=True)

mpf.plot(df, type='candle', figratio=(12,6), title='Financial Trend of Social Media and the Web - Weekly Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/15_202312252310.png'))