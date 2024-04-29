
import mplfinance as mpf
import matplotlib.pyplot as plt
import pandas as pd

data = {'Date': ['2019-06-14','2019-06-21','2019-06-28','2019-07-05','2019-07-12','2019-07-19','2019-07-26'],
        'Opening Price ($)': [75.2,77.1,76.6,76.7,77.6,78.5,80.3],
        'Closing Price ($)': [76.5,76,77.9,77.2,79.3,79.6,78.4],
        'High Price ($)': [78.2,79,79.8,78.5,80.1,81.2,81.2],
        'Low Price ($)': [74.1,74.3,75.5,75.2,76.3,77.1,77.8]}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df = df.rename(columns={'Opening Price ($)': 'Open', 
                        'Closing Price ($)': 'Close',
                        'High Price ($)': 'High',
                        'Low Price ($)': 'Low'})

plt.figure(figsize=(12,6))
mpf.plot(df, type='candle', title='Financial Trends in the Law and Legal Affairs Sector',
          figscale=2, figratio=(8,4), savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/7_202312270050.png'))