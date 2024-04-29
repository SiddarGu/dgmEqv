import pandas as pd
import mplfinance as mpf

# Define the data
data = {'Date': ['2021-05-20', '2021-05-21', '2021-05-22', '2021-05-23', '2021-05-24', '2021-05-25', '2021-05-26', '2021-05-27', '2021-05-28'],
        'Open ($)': [1320, 1318, 1323, 1324, 1330, 1329, 1333, 1345, 1347],
        'Close ($)': [1318, 1323, 1324, 1330, 1329, 1333, 1345, 1347, 1355],
        'High ($)': [1322, 1328, 1326, 1332, 1332, 1334, 1348, 1350, 1357],
        'Low ($)': [1312, 1316, 1319, 1323, 1327, 1323, 1331, 1344, 1345]}

# Create DataFrame
df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns
df.rename(columns={'Open ($)': 'Open', 'Close ($)': 'Close', 'High ($)': 'High', 'Low ($)': 'Low'}, inplace=True)

# Create figure and plot candlestick chart
fig = mpf.plot(df, type='candle', figratio=(12,6), style='yahoo', title='Business and Finance: Weekly Forex Exchange Review',
               savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/81_202312302321.png'))
