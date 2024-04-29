
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = [['2019-06-03',161.2,169.6,171.3,158.9], 
        ['2019-06-10',167.4,171.2,173.2,164.1], 
        ['2019-06-17',173.4,174.2,176.2,170.6], 
        ['2019-06-24',171.2,175.6,178.2,168.7], 
        ['2019-07-01',174.6,172.3,176.9,168.5], 
        ['2019-07-08',171.2,174.2,176.8,168.5], 
        ['2019-07-15',175.3,177.2,179.1,171.2], 
        ['2019-07-22',173.2,174.6,177.2,170.6]]

df = pd.DataFrame(data, columns = ['Date','Open','Close','High','Low'])
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

fig = plt.figure(figsize=(10,5))
mpf.plot(df, type='candle', title='Real Estate and Housing Market Trend Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/20_202312270050.png'))