
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

df = pd.DataFrame(data=[['2019-03',20,40,250,4], 
                        ['2019-04',22,38,300,6], 
                        ['2019-05',21,40,320,5], 
                        ['2019-06',23,36,350,7], 
                        ['2019-07',22,40,310,4], 
                        ['2019-08',20,38,290,6], 
                        ['2019-09',21,36,340,7], 
                        ['2019-10',23,40,320,4]], 
                   columns=['Month','Average Pay Rate ($/Hour)','Average Working Hours (Hours/Week)','Average Overtime Hours (Hours/Week)','Average Benefits ($/Month)'])
df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month',inplace=True)
df.rename(columns={'Average Pay Rate ($/Hour)':'Open', 
                    'Average Working Hours (Hours/Week)':'Close',
                    'Average Overtime Hours (Hours/Week)':'High',
                    'Average Benefits ($/Month)':'Low'}, 
           inplace=True)

mpf.plot(df, figratio=(12, 6), title='Human Resources and Employee Management Trends in Average Pay and Benefits', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/Full/candlestick/png_val/candlestick_6.png'))