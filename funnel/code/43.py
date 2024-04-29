
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [100, 88, 66, 46, 22],
    textinfo = "value+percent initial",
    orientation = "h",
    marker_color = "midnightblue",
))

fig.update_layout(
    title = "Project Development in Energy Sector in 2021",
    showlegend = True,
    legend_orientation = "h",
    margin = dict(l=200, r=200, t=50, b=50),
)

fig.update_xaxes(
    showgrid = True,
    gridwidth = 1,
    gridcolor = "LightGray",
)

fig.update_yaxes(
    showgrid = True,
    gridwidth = 1,
    gridcolor = "LightGray",
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/1.png")