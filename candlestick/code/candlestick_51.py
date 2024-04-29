import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {'Date': ['2022-01-10', '2022-01-17', '2022-01-24', '2022-01-31', '2022-02-07', '2022-02-14', '2022-02-21', '2022-02-28', '2022-03-07', '2022-03-14'],
        'Opening Price ($)': [75.0, 80, 82.0, 84, 82.3, 79.0, 82.0, 79.5, 78.0, 79.0],
        'Closing Price ($)': [78.6, 82.0, 84.0, 82.3, 79.0, 82.0, 79.5, 78.0, 79.0, 80.8],
        'High Price ($)': [80.3, 83.0, 86.0, 88.0, 84.0, 85.0, 85.0, 81.8, 82.0, 83.0],
        'Low Price ($)': [72.7, 77.0, 79.0, 80.5, 75.0, 76.0, 78.0, 76.5, 76.0, 77.2]}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.rename(columns={'Opening Price ($)': 'Open', 'Closing Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'}, inplace=True)

fig = plt.figure(figsize=(10, 6))
mpf.plot(df, type='candle', title='Weekly Stock Price Trend in Biotechnology Sector', figratio=(8, 6), savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/98_202312302321.png'))

plt.close(fig)
