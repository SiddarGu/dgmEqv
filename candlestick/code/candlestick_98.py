import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {
    'Date': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01', '2022-06-01', '2022-07-01', '2022-08-01', '2022-09-01', '2022-10-01', '2022-11-01', '2022-12-01'],
    'Open Budget (Billions)': [100, 110, 115, 111, 117, 122, 125, 127, 130, 132, 137, 140],
    'Close Budget (Billions)': [105, 112, 117, 114, 120, 124, 127, 128, 134, 135, 139, 144],
    'High Budget (Billions)': [107, 115, 121, 116, 123, 126, 129, 130, 136, 138, 142, 146],
    'Low Budget (Billions)': [98, 108, 110, 108, 115, 119, 123, 125, 129, 130, 136, 139]
}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df = df.rename(columns={
    'Open Budget (Billions)': 'Open',
    'Close Budget (Billions)': 'Close',
    'High Budget (Billions)': 'High',
    'Low Budget (Billions)': 'Low',
})

fig = plt.figure(figsize=(12, 8))
mpf.plot(df, type='candle', style='charles', title='Government Budget Allocation Trend in Year 2022', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/34_202312302321.png'))