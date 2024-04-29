
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = [['2019-08-09', 20.5, 22.3, 24.5, 18.3],
        ['2019-08-16', 23.5, 24.2, 25.1, 22.2],
        ['2019-08-23', 25.0, 26.4, 27.5, 24.2],
        ['2019-08-30', 26.7, 27.3, 28.2, 25.7],
        ['2019-09-06', 27.5, 25.2, 27.6, 23.4],
        ['2019-09-13', 24.1, 25.6, 26.9, 22.3],
        ['2019-09-20', 25.2, 26.7, 27.8, 23.4],
        ['2019-09-27', 26.9, 25.4, 27.8, 24.2]]

# Create dataframe
df = pd.DataFrame(data, columns=['Date', 'Opening Price ($)', 'Closing Price ($)', 'High Price ($)', 'Low Price ($)'])

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# Rename columns to match mplfinance column requirements
df = df.rename(columns={'Opening Price ($)': 'Open', 'Closing Price ($)': 'Close', 'High Price ($)': 'High', 'Low Price ($)': 'Low'})

plt.figure(figsize=(20,10))
mpf.plot(df, type='candle', title='Finance Trend in Law and Legal Affairs Sector', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/12_202312252310.png'))