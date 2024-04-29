
import plotly.graph_objects as go
import pandas as pd

data = {'Date':['2019-05-01','2019-05-08','2019-05-15','2019-05-22','2019-05-29'],
        'Open':[200,250,270,280,310],
        'Close':[250,275,310,320,330],
        'High':[290,320,360,370,380],
        'Low':[150,240,250,270,290]}
df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.update_layout(title='Technology and the Internet Stock Price Trend Analysis', 
                  font={'size': 10})
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/15_202312251608.png')