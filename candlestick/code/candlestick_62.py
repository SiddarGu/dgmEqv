import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {
    'Date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01', '2021-07-01', '2021-08-01', '2021-09-01', '2021-10-01', '2021-11-01', '2021-12-01'],
    'Open Enrollment Rate': [400, 440, 460, 470, 480, 520, 540, 550, 540, 580, 590, 600],
    'Closed Enrollment Rate': [450, 470, 480, 490, 500, 540, 560, 570, 560, 600, 620, 630],
    'High Enrollment Rate': [500, 510, 520, 530, 550, 580, 600, 610, 600, 650, 660, 670],
    'Low Enrollment Rate': [350, 400, 440, 420, 420, 480, 500, 500, 520, 530, 540, 570]
}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.rename(columns={
    'Open Enrollment Rate': 'Open',
    'Closed Enrollment Rate': 'Close',
    'High Enrollment Rate': 'High',
    'Low Enrollment Rate': 'Low'
}, inplace=True)

fig = plt.figure(figsize=(12, 8))
mpf.plot(df, type='candle', title='Annual Enrollment Rates Trend in Academic Institutions',
         savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/47_202312302321.png'))

plt.close(fig)
