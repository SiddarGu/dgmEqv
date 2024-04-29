
import plotly.graph_objects as go
import numpy as np

data = np.array([['2019-08-01',15.5,17.2,19.1,14.3],
['2019-08-02',17,19.5,20.2,16.3],
['2019-08-03',18,17.1,19,15.8],
['2019-08-04',17.5,17.9,19.2,15.5],
['2019-08-05',18,18.2,20,16.3],
['2019-08-06',18.5,17.9,20,16.4],
['2019-08-07',17.7,19.2,20.2,16.1]])

fig = go.Figure(data=[go.Candlestick(x=data[:,0],
                open=data[:,1],
                close=data[:,2],
                high=data[:,3],
                low=data[:,4])])

fig.update_layout(title="Share Market Performance of Environment and Sustainability Companies",
                  width=800, height=400,
                  yaxis=dict(range=[14,21]))

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/8_202312251608.png")