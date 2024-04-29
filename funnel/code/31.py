
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Research","Prototyping","Testing","Modification","Implementation"],
    x = [1000,800,600,400,200],
    textinfo = "value+percent initial",
    orientation = "h",
))
fig.update_layout(title = {"text": "Scientific Advancements in Engineering - 2021"}, font=dict(size=14))
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/25.png", scale=2, width=800, height=600)