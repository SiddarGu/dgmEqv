import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

data = {'Date': ['2021-06-01', '2021-06-08', '2021-06-15', '2021-06-22', '2021-06-29', '2021-07-06', '2021-07-13', '2021-07-20'],
        'Open Price (Hotel Rooms $)': [110, 120, 125, 140, 150, 160, 130, 140],
        'Close Price (Hotel Rooms $)': [115, 130, 140, 150, 160, 165, 120, 140],
        'High Price (Hotel Rooms $)': [140, 145, 160, 170, 180, 185, 130, 160],
        'Low Price (Hotel Rooms $)': [100, 110, 120, 130, 140, 145, 90, 130]}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

df = df.rename(columns={'Open Price (Hotel Rooms $)': 'Open', 
                        'Close Price (Hotel Rooms $)': 'Close', 
                        'High Price (Hotel Rooms $)': 'High', 
                        'Low Price (Hotel Rooms $)': 'Low'})

fig = plt.figure(figsize=(12, 8))

mpf.plot(df, type='candle', title='Hotel Room Rate Movements for Summer 2021',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/79_202312302321.png'))

plt.close(fig)
