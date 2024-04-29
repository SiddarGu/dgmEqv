
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {'Date':['2020-08-12','2020-08-19','2020-08-26','2020-09-02','2020-09-09','2020-09-16','2020-09-23','2020-09-30'],
        'Opening Price ($)' : [40,45,45.7,47,50,51.5,51,46],
        'Closing Price ($)' : [41.6,44,45.2,48.2,51.2,53.2,48,48.6],
        'High Price ($)' : [45,47,48.2,49.5,53.1,56,52,49.3],
        'Low Price ($)' : [38,41,43,45.2,47.5,50.4,45,44.5]
        }

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df = df.rename(columns={"Opening Price ($)": "Open", "Closing Price ($)": "Close", "High Price ($)": "High", "Low Price ($)": "Low"})

fig = plt.figure(figsize=(12,6))
mpf.plot(df, type='candle', style='charles', figratio=(12,6), title='Financial Performance of Nonprofit Organizations - Weekly Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/13_202312252310.png'))