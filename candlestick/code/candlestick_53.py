import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {
    'Date': ['2021-02-01', '2021-02-08', '2021-02-15', '2021-02-22',
             '2021-03-01', '2021-03-08', '2021-03-15', '2021-03-22'],
    'Opening Price ($)': [60.3, 66.2, 68, 72, 75, 78, 81, 84],
    'Closing Price ($)': [65.9, 67.4, 70.9, 74.1, 77.2, 80.3, 83.3, 86.3],
    'High Price ($)': [67.2, 70, 71.5, 76.2, 79.4, 82.4, 85.4, 88.4],
    'Low Price ($)': [58.7, 63.5, 66.8, 70.8, 73.6, 76.8, 79.8, 82.8]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df = df.rename(columns={
    'Opening Price ($)': 'Open', 
    'Closing Price ($)': 'Close',
    'High Price ($)': 'High',
    'Low Price ($)': 'Low'
})

fig = plt.figure(figsize=(11, 9))

mpf.plot(df, type='candle', style='starsandstripes', title='Weekly Stock Price Movements of a Leading Sports & Entertainment Company',
         figratio=(8,6), savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/31_202312302321.png'))

plt.close(fig)
