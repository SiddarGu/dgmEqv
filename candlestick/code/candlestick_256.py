
import plotly.graph_objects as go
import plotly.express as px

fig = go.Figure(data=[go.Candlestick(x=["2019","2020","2021","2022","2023"],
                open=[20.3,17.9,18.5,19.2,18.7],
                high=[20.3,17.9,18.5,19.2,18.7],
                low=[1.2,0.8,1.1,1.5,1.3],
                close=[3.7,4.3,3.9,3.4,3.7])])

fig.update_layout(title="Financial Trends in Social Sciences and Humanities Over the Years",
                  xaxis_title="Year",
                  yaxis_title="Value",
                  yaxis_range=[0,20.5],
                  width=800,
                  height=600,
                  font=dict(family="Courier New, monospace", size=12, color="#7f7f7f"))

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/3_202312270043.png")