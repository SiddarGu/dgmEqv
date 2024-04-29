import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {
    'Date': ['2021-01-04', '2021-01-11', '2021-01-18', '2021-01-25', '2021-02-01', '2021-02-08', '2021-02-15',
             '2021-02-22', '2021-03-01', '2021-03-08', '2021-03-15', '2021-03-22', '2021-03-29', '2021-04-05',
             '2021-04-12', '2021-04-19', '2021-04-26'],
    'Open Price ($)': [37.6, 37.1, 39.3, 39.6, 40.8, 42.1, 43.4, 43.6, 44.6, 45.8, 46.4, 46.6, 47.8, 48.1, 47.9, 48.3, 48.4],
    'Close Price ($)': [36.9, 38.7, 40.1, 39.8, 41.3, 42.5, 43.3, 44.4, 45.5, 46.5, 46.2, 47.3, 48.1, 47.9, 48.7, 48.1, 49.3],
    'High Price ($)': [38.5, 39.2, 40.5, 41.2, 42.5, 43.7, 44.7, 45.8, 46.9, 47.7, 48.5, 48.9, 49.5, 50.3, 50.1, 50.5, 51.7],
    'Low Price ($)': [36.2, 35.5, 37.8, 38.1, 39.4, 41.1, 42.9, 43.1, 43.6, 44.1, 45.8, 46, 46.8, 47, 47.1, 47.3, 47.9]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df = df.rename(columns={'Open Price ($)': 'Open', 'Close Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'})

mpf.plot(df, type='candle', figratio=(12,6), title='Food and Beverage Industry: Stock Price Analysis of 2021 First Quarter', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/97_202312302321.png'), style='binance')
