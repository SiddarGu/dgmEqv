
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

df = pd.DataFrame({
    'Date': ['2019-05-14', '2019-05-21', '2019-05-28', '2019-06-04', '2019-06-11', '2019-06-18', '2019-06-25'],
    'Opening Price ($)': [11.5, 11.3, 12.2, 11.9, 12.4, 12.3, 11.5],
    'Closing Price ($)': [11.2, 11.6, 11.8, 12.1, 12.7, 12, 12.2],
    'High Price ($)': [12, 12.5, 12.7, 12.3, 13, 12.5, 12.7],
    'Low Price ($)': [10.8, 10.9, 11, 11.5, 11.7, 11.6, 11.2]
})

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.rename(columns={
    'Opening Price ($)': 'Open', 
    'Closing Price ($)': 'Close',
    'High Price ($)': 'High',
    'Low Price ($)': 'Low'
}, inplace=True)

mpf.plot(df, type='candle', figratio=(12, 6), title='Financial Trend of Charity and Nonprofit Organizations', figscale=2, savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/3_202312270050.png'))