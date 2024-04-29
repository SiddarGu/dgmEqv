import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf

# Create DataFrame
data = {'Date': ['2020-03-01', '2020-03-08', '2020-03-15', '2020-03-22', '2020-03-29', '2020-04-05', '2020-04-12', '2020-04-19', '2020-04-26'],
        'Open Price': [500, 530, 545, 575, 595, 610, 635, 655, 677],
        'Close Price': [525, 542, 560, 590, 605, 630, 650, 670, 690],
        'High Price': [540, 560, 570, 600, 620, 640, 655, 685, 700],
        'Low Price': [490, 520, 540, 570, 580, 600, 625, 650, 670]}

df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns
df.rename(columns={'Open Price': 'Open', 'Close Price': 'Close', 'High Price': 'High', 'Low Price': 'Low'}, inplace=True)

# Plot candlestick chart
mpf.plot(df, type='candle', style='classic', title='Weekly Trend of Engineering Equipment Stock Prices', figratio=(12,6),
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/68_202312302321.png'))
