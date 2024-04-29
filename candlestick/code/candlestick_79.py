import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {'Date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01'],
        'Open Tuition Fee ($)': [15000, 16000, 16500, 17500, 18000, 18500],
        'Close Tuition Fee ($)': [14500, 15000, 17000, 18000, 18500, 19000],
        'High Tuition Fee ($)': [15500, 16500, 17500, 18500, 19000, 19500],
        'Low Tuition Fee ($)': [14000, 15000, 16000, 17500, 18000, 18500]}

df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

df = df.rename(columns={'Open Tuition Fee ($)': 'Open',
                        'Close Tuition Fee ($)': 'Close',
                        'High Tuition Fee ($)': 'High',
                        'Low Tuition Fee ($)': 'Low'})

fig = plt.figure(figsize=(10, 6))

mpf.plot(df, type='candle', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/53_202312302321.png'), figratio=(12,6), style='yahoo', title='Monthly Tuition Fee Trend for 2021 in the Education Sector')