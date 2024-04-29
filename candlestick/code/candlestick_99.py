
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = [['2021-05-03',20,19.5,21.2,18.2],
        ['2021-05-10',21,19.8,21.6,18.5],
        ['2021-05-17',23,21.4,23.5,20.4],
        ['2021-05-24',22,20.8,22.5,19.2],
        ['2021-05-31',20.5,21.2,22.5,17.9],
        ['2021-06-07',22,20.5,22.2,19.7],
        ['2021-06-14',20.5,19.5,21.5,18.5],
        ['2021-06-21',19,19.2,20.2,17]]

df = pd.DataFrame(data,columns=['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)
df.rename(columns={'Opening Price ($)':'Open','Closing Price ($)':'Close','High Price ($)':'High','Low Price ($)':'Low'},inplace=True)

fig = plt.figure(figsize=(12,6))
mpf.plot(df,type='candle',style='charles',title='Financial Trend of Energy and Utilities Sector',savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/5_202312270050.png'))