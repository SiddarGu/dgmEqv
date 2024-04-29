
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

df = pd.DataFrame(data=[[50.5, 52, 54.2, 49.8], [53, 52.1, 55.2, 51.9], [53,52,53,50.7], [54,55.7,56.6,53.4], [55,56.9,57.2,54]], index=pd.to_datetime(['2019-04-26', '2019-04-27', '2019-04-28', '2019-04-29', '2019-04-30']), columns=['Opening Price ($/MWh)', 'Close Price ($/MWh)', 'High Price ($/MWh)', 'Low Price ($/MWh)'])
df.rename(columns={'Opening Price ($/MWh)': 'Open', 'Close Price ($/MWh)': 'Close', 'High Price ($/MWh)': 'High', 'Low Price ($/MWh)': 'Low'}, inplace=True)
mpf.plot(df, type='candle', figsize=(15,7), title='Energy and Utilities Industry - Power Prices Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/21_202312270050.png'))