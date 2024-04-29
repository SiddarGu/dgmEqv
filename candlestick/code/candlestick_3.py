
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf

data = {'Date':['2019-08-26','2019-08-27','2019-08-28','2019-08-29','2019-08-30','2019-09-01','2019-09-02'],
        'Opening Price ($)':[56.2,58.5,60.3,61.5,58,59.4,58.2], 
        'Closing Price ($)':[58.3,59.9,62.1,58.4,60.9,61.1,62.3], 
        'High Price ($)':[59.4,61.1,64.2,63.2,64.2,62.6,63.2], 
        'Low Price ($)':[53.2,56.3,59.1,57.2,56.4,54.3,56.1]}

df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
df.rename(columns={'Opening Price ($)':'Open', 'Closing Price ($)':'Close', 'High Price ($)':'High', 'Low Price ($)':'Low'}, inplace=True)

mpf.plot(df,
        type='candle', figratio=(12,6), 
        title='Financial Trend of Education and Academics Industry - Weekly Overview',
        savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/10_202312252310.png'))