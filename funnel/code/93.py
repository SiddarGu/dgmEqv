
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Discovery", "Interest", "Research", "Purchase", "Consumption", "Retention"],
    x = [1000, 900, 800, 700, 500, 300],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["royalblue", "crimson", "orange", "lightgreen", "lightseagreen", "gold"]},
))

fig.update_layout(
    title = {"text": "Sports and Entertainment Experiences in 2021", "y":0.9, "x":0.5, "xanchor": "center", "yanchor": "top"},
    font=dict(family="Courier New, monospace", size=14, color="#7f7f7f"),
    width=800,
    height=650,
    showlegend=False
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/66.png")