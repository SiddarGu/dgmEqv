
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Discovery", "Research", "Shopping", "Purchase", "Feedback"],
    x = [100.00, 88.80, 66.60, 46.20, 22.80],
    textinfo = "value+percent initial",
    textfont_size = 10,
    opacity = 0.8,
    marker = {"color": ["#3D9970", "#FF4136", "#FF851B", "#85144B", "#B10DC9"]},
))

fig.update_layout(
    title_text = "Consumer Journey in Food and Beverage Industry in 2021",
    font = {"family": "Courier New, monospace", "size": 12},
    showlegend = False,
    yaxis_title = "Stage",
    xaxis_title = "Number of Customers",
    margin = dict(l=200, r=200, t=100, b=100),
    width=800,
    height=700,
)
fig.layout.xaxis.tickfont.size = 8
fig.layout.yaxis.tickfont.size = 10
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/99.png")