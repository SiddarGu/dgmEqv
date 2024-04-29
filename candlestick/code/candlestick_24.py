
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

data = [['2020-07-14',72,71.2,73.6,70.4],
        ['2020-07-21',70.5,72.3,73.1,69.4],
        ['2020-07-28',73,71.9,73.4,69.2],
        ['2020-08-04',70.3,72.5,73.1,69.4],
        ['2020-08-11',73.4,71.2,74.2,69.8],
        ['2020-08-18',69.2,73.1,74.2,68.4],
        ['2020-08-25',71.9,72.4,73.8,70.5]]

df = pd.DataFrame(data, columns=['Date', 'Opening Price ($)', 'Closing Price ($)', 'High Price ($)', 'Low Price ($)'])
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df.rename(columns={'Opening Price ($)':'Open', 'Closing Price ($)':'Close', 'High Price ($)':'High', 'Low Price ($)':'Low'}, inplace=True)

fig = plt.figure(figsize=(15,7))
mpf.plot(df, type='candle', style='charles', title='Weekly Change in Logistics and Transportation Stock Price', ylabel='Price ($)', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/13_202312270050.png'))