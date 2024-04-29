
import plotly.express as px
import plotly.graph_objects as go

data = [
    ["2021-05-11",50.3,53.2,54.2,48],
    ["2021-05-18",54,57.1,58.7,51],
    ["2021-05-25",55,56.7,59.6,53.2],
    ["2021-06-01",58.3,57.2,60.1,54],
    ["2021-06-08",53.5,55.2,56.1,50.2],
    ["2021-06-15",60,59.9,63.2,57.2],
    ["2021-06-22",54.5,53,55.3,50.2] 
]

fig = go.Figure(data=[go.Candlestick(x=[row[0] for row in data], open=[row[1] for row in data],close=[row[2] for row in data],high=[row[3] for row in data],low=[row[4] for row in data])])

fig.update_layout(title="Energy and Utilities Financial Trends Overview", width=1200, height=800, yaxis_range=[min([row[-1] for row in data]), max([row[3] for row in data])])
fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/29_202312252244.png")