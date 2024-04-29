
import plotly.express as px
import plotly.graph_objects as go

data = [go.Candlestick(x=["2019-06-20","2019-06-27","2019-07-04","2019-07-11","2019-07-18","2019-07-25"],
                       open=[14.3,12.9,14.1,15.5,14.8,15.2],
                       high=[15.2,15.2,15.6,16.2,15.5,15.8],
                       low=[12.5,12.2,12.5,13.7,12.9,13.8],
                       close=[13.9,14.5,15.2,14.9,15.2,14.7])]

fig = go.Figure(data)
fig.update_layout(title_text="Financial Performance of Education and Academics Sector - Weekly Overview",
                  width=700,
                  height=500,
                  yaxis_range=[12,17])
fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/21_202312252244.png")