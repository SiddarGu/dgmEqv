
import plotly.graph_objects as go
import datetime

data = [("2020-11-12",80,80.9,81.5,79.5),
        ("2020-11-19",81,81.7,82.3,79.5),
        ("2020-11-26",80.5,81.2,82.2,79.8),
        ("2020-12-03",82,83.2,83.7,81.3),
        ("2020-12-10",82.5,83.8,84.8,81.8),
        ("2020-12-17",83,83.5,84.8,81.9),
        ("2020-12-24",83.2,83.5,84.7,81.5),
        ("2020-12-31",84.3,85.2,86.1,83.6)]

x = [datetime.datetime.strptime(date, "%Y-%m-%d").date() for (date,open_p,close_p,high_p,low_p) in data]
open_p = [open_p for (date,open_p,close_p,high_p,low_p) in data]
close_p = [close_p for (date,open_p,close_p,high_p,low_p) in data]
high_p = [high_p for (date,open_p,close_p,high_p,low_p) in data]
low_p = [low_p for (date,open_p,close_p,high_p,low_p) in data]

fig = go.Figure(data=[go.Candlestick(x=x,
                open=open_p,
                high=high_p,
                low=low_p,
                close=close_p)])

fig.update_layout(
    title="Education and Academics Stock Performance - 8 Weeks Overview",
    xaxis_title="Date",
    yaxis_title="Price ($)",
    width=1800,
    height=1000,
    yaxis_range=[79,87],
    font=dict(family="Courier New", size=16, color="#7f7f7f")
)

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/11_202312252244.png")