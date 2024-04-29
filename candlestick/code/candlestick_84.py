import pandas as pd
import mplfinance as mpf

# Create DataFrame
df = pd.DataFrame({
    'Date': ['2017-05-01', '2017-05-08', '2017-05-15', '2017-05-22', '2017-05-29'],
    'Opening Price ($)': [148.3, 156, 168.9, 177.4, 187.1],
    'Closing Price ($)': [156.7, 168.9, 177.4, 187.1, 195.4],
    'High Price ($)': [158.2, 173, 180.2, 190.2, 200],
    'Low Price ($)': [147, 155.7, 167, 175, 185.7]
})

# Convert 'Date' to datetime and set as index
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

# Rename columns
df = df.rename(columns={
    'Opening Price ($)': 'Open',
    'Closing Price ($)': 'Close',
    'High Price ($)': 'High',
    'Low Price ($)': 'Low'
})

# Plot candlestick chart
mpf.plot(df, type='candle', style='yahoo', title='Tech Giant\'s Stock Performance in May 2017', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/59_202312302321.png'))
