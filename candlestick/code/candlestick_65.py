import pandas as pd
import mplfinance as mpf

data = [['2020-01-01', 60000, 60500, 61000, 59000],
        ['2020-02-01', 60500, 61000, 61500, 60100],
        ['2020-03-01', 61000, 61200, 62000, 60000],
        ['2020-04-01', 61300, 62000, 62500, 60400],
        ['2020-05-01', 62500, 63500, 64000, 61750],
        ['2020-06-01', 63600, 64500, 65000, 63000],
        ['2020-07-01', 64600, 65200, 65500, 64000],
        ['2020-08-01', 65400, 66000, 66500, 64500],
        ['2020-09-01', 66100, 66500, 67000, 65000],
        ['2020-10-01', 66550, 67000, 67500, 66000],
        ['2020-11-01', 67050, 67500, 68000, 66500],
        ['2020-12-01', 67600, 68000, 68500, 67000]]

df = pd.DataFrame(data, columns=['Date', 'HR Budget Opening ($)', 'HR Budget Closing ($)', 'HR Budget High ($)', 'HR Budget Low ($)'])

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

df = df.rename(columns={'HR Budget Opening ($)': 'Open',
                        'HR Budget Closing ($)': 'Close',
                        'HR Budget High ($)': 'High',
                        'HR Budget Low ($)': 'Low'})

mpf.plot(df, type='candle', style='charles', title='Monthly HR Budget Forecast Trends in 2020',
         figratio=(10,6), savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/38_202312302321.png'))