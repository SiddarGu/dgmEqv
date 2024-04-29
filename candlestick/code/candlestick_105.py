import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {'Date': ['2023-06-01', '2023-06-02', '2023-06-03', '2023-06-04', '2023-06-05', '2023-06-06', '2023-06-07', '2023-06-08', '2023-06-09', '2023-06-10'],
        'Opening Price ($)': [120.5, 126, 128, 124, 123.2, 122, 124, 126, 125.2, 124.5],
        'Closing Price ($)': [125.7, 127.5, 125, 123.2, 122, 123.5, 125.6, 125.2, 124.5, 126.7],
        'High Price ($)': [130.2, 132.2, 130, 130.5, 128.9, 127.2, 128.9, 130.5, 129.5, 131],
        'Low Price ($)': [120, 124, 124.7, 122.9, 122, 121, 123.7, 125.2, 124, 124]}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df = df.rename(columns={'Opening Price ($)': 'Open', 'Closing Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'})

mpf.plot(df, type='candle', title='Social Media Stock Price Fluctuations - 10 Day Analysis', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/110_202312302321.png'))