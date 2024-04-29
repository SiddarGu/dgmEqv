
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Initial Research","Product Comparison","Product Selection","Trial Period","Purchase","Retention"],
    x = [20000,15000,10000,8000,6000,4000],
    textinfo = "value+percent initial",
    marker_opacity = 0.7,
    marker = {"color": ["rgb(50,50,51)","rgb(76,175,80)","rgb(244,67,54)","rgb(33,150,243)","rgb(255,235,59)","rgb(139,195,74)"]}
))
fig.update_layout(
    title = {"text": "Online Shopping in Technology and the Internet in 2021"},
    margin = {"l": 200, "r": 200, "t":200, "b":200},
    font = {"family": "Courier New, monospace", "size": 16},
    showlegend = False,
    width = 800,
    height = 800
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/77.png")