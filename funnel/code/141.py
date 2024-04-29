
import plotly.graph_objects as go

data = [go.Funnel(
    y = ["Research and Development", "Design and Prototype", "Refinement and Testing", "Production and Delivery", "Maintenance and Upgrades", "Others"],
    x = [200, 170, 140, 110, 80, 50],
    textinfo = "value+percent initial",
    marker = {"color": ["#EF5350", "#FFCA28", "#66BB6A", "#29B6F6", "#AB47BC", "#9C27B0"]},
    opacity = 0.8
)]

layout = go.Layout(
    title = {"text": "Science and Engineering Projects in 2021"},
    width = 1200,
    height = 800,
    legend = {"x": 0.1, "y": 1},
    paper_bgcolor = "rgba(0,0,0,0)",
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis = {"visible": True},
    yaxis = {"visible": True},
    showlegend = True
)

fig = go.Figure(data = data, layout = layout)

fig.write_image("../png/141.png")