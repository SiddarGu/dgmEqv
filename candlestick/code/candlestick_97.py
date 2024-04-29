
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

df = pd.DataFrame([['2019-05-01',30,32.1,33.2,29.3],
                  ['2019-05-08',31.5,33.2,34.4,30.8],
                  ['2019-05-15',35.4,36.8,38.5,34],
                  ['2019-05-22',35.6,37.2,38.1,33.5],
                  ['2019-05-29',37,38.5,39.5,36.4],
                  ['2019-06-05',39.5,41.2,42.3,38.2],
                  ['2019-06-12',41,41.1,42.8,39.7],
                  ['2019-06-19',40,41.2,42.4,38.3]],
                  columns = ['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df = df.rename(columns={'Opening Price ($)':'Open','Closing Price ($)':'Close','High Price ($)':'High','Low Price ($)':'Low'})

mpf.plot(df,type='candle', figratio=(12,6),title='Transportation and Logistics Stock Performance - Weekly Overview',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/17_202312270050.png'))