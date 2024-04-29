
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Research", "Planning", "Implementation", "Maintenance", "Expansion"],
    x = [100, 80, 60, 40, 20],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.8,
    marker = {"color": ["#f2bc06", "#0095b6", "#7dbf3f", "#a66421", "#2f4d6c"]},
    width = 0.5
))

fig.update_layout(
    title = {"text": "Energy and Utilities Projects in 2021", "y": 0.96, "x": 0.5, "xanchor": "center", "yanchor": "top"},
    font = {"family": "Courier New"},
    width = 1000,
    height = 800,
    showlegend = True,
    paper_bgcolor = "rgba(0,0,0,0)",
    plot_bgcolor = "rgba(0,0,0,0)",
    margin = go.layout.Margin(
        l = 25,
        r = 25,
        b = 25,
        t = 25,
        pad = 4
    ),
    legend = go.layout.Legend(
        x = 0.75,
        y = -0.1
    )
)

fig.write_image("../png/46.png")