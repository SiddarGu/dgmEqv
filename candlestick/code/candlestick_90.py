import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {
    'Date': ['2021-05-01', '2021-05-02', '2021-05-03', '2021-05-04', '2021-05-05', '2021-05-06', '2021-05-07', '2021-05-08'],
    'Open Price ($)': [85, 91, 96, 94.5, 101, 106, 111, 113],
    'Close Price ($)': [90, 95.1, 94, 100.7, 105.5, 110, 112, 115],
    'High Price ($)': [93, 99, 101, 102, 108, 114, 118, 120],
    'Low Price ($)': [82, 88, 90, 92, 99.5, 104, 110, 111.5]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

df = df.rename(columns={
    'Open Price ($)': 'Open',
    'High Price ($)': 'High',
    'Low Price ($)': 'Low',
    'Close Price ($)': 'Close'
})

mpf.plot(df, type='candle', show_nontrading=False, title='Transportation and Logistics Stock Trends for May 2021', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/54_202312302321.png'))
