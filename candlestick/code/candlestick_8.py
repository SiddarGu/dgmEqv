
import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt

data = {'Year':[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018],
        'Gross Domestic Product ($Billion)':[14.6, 15.2, 15.8, 16.6, 17.2, 17.5, 18.1, 18.6, 19.2],
        'Unemployment Rate (% of Labour Force)':[27.6, 27.9, 27.4, 27.1, 26.2, 26.2, 25.7, 24.7, 24.1],
        'Inflation Rate (%)':[3.5, 2.4, 1.7, 2.7, 3.6, 2.3, 2.5, 2.3, 2.2],
        'Debt (% of GDP)':[24, 22, 20, 19, 20, 19, 19, 17, 16]}

df = pd.DataFrame(data)
df['Date'] = df['Year'].apply(lambda x: str(x)+ '-12-31')
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df = df.rename(columns={'Gross Domestic Product ($Billion)':'Open', 'Unemployment Rate (% of Labour Force)':'High', 
                        'Inflation Rate (%)':'Low', 'Debt (% of GDP)':'Close'})

mpf.plot(df, type='candle', style='charles', figratio=(12, 6), title='Financial Trends in Social Sciences and Humanities Over the Years',
          ylabel='Price ($)', ylabel_lower='', figscale=1.5, savefig=dict(fname='/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_mplfinance/png/4_202312252310.png'))