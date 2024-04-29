
import plotly.graph_objects as go
from datetime import datetime

data = [[datetime(2020, 7, 10), 213.2, 220.4, 223.4, 210.1],
        [datetime(2020, 7, 17), 220.8, 217.2, 221.5, 213.6],
        [datetime(2020, 7, 24), 216.3, 212.2, 218.7, 210.2],
        [datetime(2020, 7, 31), 210.7, 218.1, 220.9, 207.6],
        [datetime(2020, 8, 7), 217.8, 219.7, 221.2, 215.2],
        [datetime(2020, 8, 14), 218.9, 221.8, 223.4, 216.2],
        [datetime(2020, 8, 21), 222.2, 219.5, 223.7, 216.7],
        [datetime(2020, 8, 28), 219.2, 214.1, 221.2, 212.0]]

fig = go.Figure(data=[go.Candlestick(x=[date[0] for date in data],
                       open=[date[1] for date in data],
                       close=[date[2] for date in data],
                       high=[date[3] for date in data],
                       low=[date[4] for date in data])])

fig.update_layout(title='Healthcare Stock Price Trend in August 2020',
                 yaxis_range=[210, 225],
                 width=960,
                 height=540,
                 font=dict(size=10))

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/14_202312252244.png")