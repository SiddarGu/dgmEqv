import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {'Date': ['2020-12-31', '2021-01-01', '2021-02-01', '2021-02-02', '2021-03-01', '2021-03-02', '2021-04-01', '2021-05-01', '2021-06-01', '2021-07-01', '2021-08-01', '2021-09-01'],
        'Open Donation ($)': [750, 800, 820, 700, 650, 590, 550, 530, 600, 650, 630, 610],
        'Close Donation ($)': [810, 850, 800, 810, 600, 620, 600, 500, 650, 630, 610, 620],
        'High Donation ($)': [830, 890, 870, 840, 700, 650, 640, 540, 670, 670, 660, 640],
        'Low Donation ($)': [650, 770, 790, 650, 580, 570, 530, 500, 590, 600, 600, 600]}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df = df.rename(columns={'Open Donation ($)': 'Open', 'Close Donation ($)': 'Close', 'High Donation ($)': 'High', 'Low Donation ($)': 'Low'})

fig = plt.figure(figsize=(10, 6))
mpf.plot(df, type='candle', style='charles', title='Monthly Donation Range in a Nonprofit Organization', figratio=(10, 6), savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/36_202312302321.png'))