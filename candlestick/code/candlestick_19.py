
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = [['2019-04-20',49.9,51.3,53.2,48.2],
        ['2019-04-21',52,51.2,53.4,50.1],
        ['2019-04-22',52.8,51.2,54.3,50.7],
        ['2019-04-23',50.7,51.8,53.1,49.2],
        ['2019-04-24',52.4,53.7,54.6,50.2],
        ['2019-04-25',53.3,54.9,56.3,51.2],
        ['2019-04-26',54.1,55.9,57.8,52.5]]

df = pd.DataFrame(data, columns = ['Date', 'Opening Price ($)', 'Closing Price ($)', 'High Price ($)', 'Low Price ($)'])
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index(df['Date'])
df = df.rename(columns = {'Opening Price ($)':'Open', 'Closing Price ($)':'Close', 'High Price ($)':'High', 'Low Price ($)':'Low'})

plt.figure(figsize=(14,10))
mpf.plot(df, type='candle', title='Financial Trend in Tourism and Hospitality Sector Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/23_202312252310.png'))