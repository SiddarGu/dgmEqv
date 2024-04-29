
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

data = {'Month': ['2019-05', '2019-06', '2019-07', '2019-08', '2019-09', '2019-10', '2019-11'],
       'Opening Price (USD)': [75000, 78000, 77000, 78000, 80000, 82000, 83000],
       'Closing Price (USD)': [72500, 77000, 77000, 80000, 81500, 83000, 84000],
       'High Price (USD)': [78000, 80000, 78500, 81500, 83000, 85000, 86000],
       'Low Price (USD)': [68000, 70000, 72500, 75000, 79000, 79000, 80000]}

df = pd.DataFrame(data)
df['Month'] = pd.to_datetime(df['Month'])
df.set_index('Month', inplace=True)
df = df.rename(columns={'Opening Price (USD)': 'Open', 'Closing Price (USD)': 'Close',
                        'High Price (USD)': 'High', 'Low Price (USD)': 'Low'})

mpf.plot(df, type='candle', figratio=(12,6), title='Real Estate and Housing Market Performance - Monthly Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/20_202312252310.png'))