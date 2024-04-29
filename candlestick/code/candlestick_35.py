
import plotly.graph_objects as go
import pandas as pd

data = [['2019-04-26', 20.5, 21.3, 23.1, 19.1], 
        ['2019-04-27', 22.1, 20.7, 23.2, 19.9], 
        ['2019-04-28', 21.9, 22.4, 25.6, 20.3], 
        ['2019-04-29', 23.2, 22.8, 25.7, 21.5], 
        ['2019-04-30', 22.9, 24.5, 26.0, 22.1], 
        ['2019-05-01', 25.0, 24.2, 26.2, 21.9], 
        ['2019-05-02', 23.5, 24.8, 25.6, 22.1], 
        ['2019-05-03', 25.2, 25.4, 27.1, 23.4]]

df = pd.DataFrame(data, columns=['Date', 'Open', 'Close', 'High', 'Low'])
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                       open=df['Open'], 
                       high=df['High'], 
                       low=df['Low'], 
                       close=df['Close'])])

fig.update_layout(title='Technology and the Internet Stock Market Trend Overview',
                  xaxis_title='Date',
                  yaxis_title='Price ($)',
                  yaxis_range=[19, 27.5],
                  width=800,
                  height=400,
                  font={'family': 'Helvetica', 'size': 16})

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/20_202312252244.png')