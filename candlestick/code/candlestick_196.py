
import plotly.graph_objects as go
import pandas as pd

fig = go.Figure(data=[go.Candlestick(x=pd.date_range(start='2020-04-26', end='2020-04-30'),
                open= [17.9,19.3,19.1,19.9,21.7],
                high= [21.2,20,20.7,22.2,24.2],
                low= [15.2,17.2,15.9,18.3,19.6],
                close= [19.6,18.8,19.5,21.5,22.9])])

fig.update_layout(title_text='Energy Commodities Price Development - Five Day Overview',
                  width=600, 
                  height=400, 
                  yaxis_range=[15.2,24.2])

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/12_202312270043.png')