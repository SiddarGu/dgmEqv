
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance

data = [['2019-04-26',50.5,52,54.2,49.8],
        ['2019-04-27',53,52.1,55.2,51.9],
        ['2019-04-28',53,52,53,50.7],
        ['2019-04-29',54,55.7,56.6,53.4],
        ['2019-04-30',55,56.9,57.2,54],
        ['2019-05-01',58.3,60.3,60.6,56.2],
        ['2019-05-02',60,62.3,63.2,59.4],
        ['2019-05-03',61.2,64.2,64.5,60.8],
        ['2019-05-04',63.5,63.7,66.3,62.3],
        ['2019-05-05',62,63.4,64.2,61]]

df = pd.DataFrame(data, columns = ['Date', 'Opening Price ($)', 'Closing Price ($)', 'High Price ($)', 'Low Price ($)'])
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df.rename(columns = {'Opening Price ($)':'Open', 
                     'Closing Price ($)':'Close', 
                     'High Price ($)':'High', 
                     'Low Price ($)':'Low'}, inplace = True)

plt.figure(figsize=(14, 10))
mplfinance.plot(df, type='candle', title = 'Social Media and Web Stock Performance Overview', savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/9_202312252310.png'))