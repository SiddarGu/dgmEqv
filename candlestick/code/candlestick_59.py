import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

# Define the data
data = {
    'Date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01',
             '2020-08-01', '2020-09-01', '2020-10-01', '2020-11-01', '2020-12-01'],
    'Open Budget ($bn)': [500, 510, 520, 525, 523, 535, 540, 545, 555, 560, 570, 575],
    'Final Budget ($bn)': [510, 520, 525, 523, 535, 540, 545, 555, 560, 570, 575, 580],
    'Highest Proposed Budget ($bn)': [520, 530, 550, 540, 550, 560, 565, 575, 580, 590, 595, 600],
    'Lowest Proposed Budget ($bn)': [480, 500, 510, 510, 515, 520, 515, 535, 540, 550, 555, 560]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Rename columns to match mplfinance requirements
df.rename(columns={
    'Open Budget ($bn)': 'Open',
    'Highest Proposed Budget ($bn)': 'High',
    'Lowest Proposed Budget ($bn)': 'Low',
    'Final Budget ($bn)': 'Close'
}, inplace=True)

mpf.plot(df, type='candle', figratio=(12,6), style='yahoo', title='Monthly Government Budgeting Process in Year 2020', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/50_202312302321.png'))

