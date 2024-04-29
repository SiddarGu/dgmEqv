import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

data = {'Date': ['2022-01-01', '2022-01-08', '2022-01-15', '2022-01-22', '2022-01-29', '2022-02-05'],
        'Opening Price ($)': [34.5, 38, 40, 45, 47, 51],
        'Closing Price ($)': [37, 39.5, 42, 46, 50, 53],
        'High Price ($)': [39.2, 41, 44.3, 49.5, 52.6, 55.3],
        'Low Price ($)': [32, 35, 39, 43.5, 45, 49]}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.rename(columns={'Opening Price ($)': 'Open', 'Closing Price ($)': 'Close', 
                   'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

fig = plt.figure(figsize=(10, 6))
mpf.plot(df, type='candle', style='yahoo', figratio=(6, 1.5), title='Auction House Art Performance: Weekly Price Trends',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/124_202312302321.png'))

plt.close(fig)
