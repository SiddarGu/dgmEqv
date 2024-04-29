
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [1000, 900, 800, 700, 600],
    textinfo = "value+percent initial",
    opacity = 0.7,
    marker = {"color": ["red", "green", "blue", "yellow", "orange"]},
    text = ["1000", "900", "800", "700", "600"],
    textposition = "inside",
    hoverinfo = "text"
))
fig.update_layout(
    title = "User Engagement in Social Media in 2020",
    font = {"family": "Courier New, monospace", "size": 20},
    shapes = [
        {"type": "line", "x0": -0.5, "y0": -0.5, "x1": 1.5, "y1": -0.5, "line": {"width": 1, "color":"LightGrey"}},
    ],
    showlegend = False,
    legend_orientation="h",
    legend_xanchor = "center",
    legend_yanchor = "top",
    legend_x = 0.5,
    legend_y = 1.1,
    autosize = True,
    width = 800,
    height = 600,
    margin = {"l": 10, "r": 10, "t": 40, "b": 10},
    paper_bgcolor = "rgba(0,0,0,0)",
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis = {"showgrid": False, "zeroline": False},
    yaxis = {"showgrid": False, "zeroline": False},
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/30.png")