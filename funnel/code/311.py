
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [100, 80, 60, 40, 20],
    textinfo = "value+percent initial",
    marker = dict(
        color = ["#d3d3d3", "#b3b3b3", "#a2a2a2", "#8f8f8f", "#7f7f7f"],
        line = dict(
            color = ["#d3d3d3", "#b3b3b3", "#a2a2a2", "#8f8f8f", "#7f7f7f"],
            width = 3
        )
    ),
    textfont = dict(size = 15),
    opacity = 0.7,
    connector = {"line":{"color":"#000000", "dash":"solid"}},
    hoverinfo = "none"
))

fig.update_layout(
    title = {"text":"Real Estate Market Activity in 2021"},
    font = dict(family = "sans-serif"),
    showlegend = False,
    width = 1000,
    height = 800,
    yaxis_title = "Stage",
    xaxis_title = "Number of Properties",
    grid = {"rows": 1, "columns": 1, "pattern": "independent"}
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/27.png")