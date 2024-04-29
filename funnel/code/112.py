
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [5000000, 4000000, 3000000, 2000000, 1000000],
    textinfo = "value+percent initial",
    marker_color = "blue",
    opacity = 0.7
))

fig.update_layout(
    title = "Technology and the Internet Usage in 2020",
    font = dict(
        size = 10
    ),
    width = 500,
    height = 600,
    margin = dict(
        l = 0,
        r = 0,
        t = 30,
        b = 0
    ),
    legend = dict(
        orientation = "h",
        yanchor = "top",
        y = 1.02,
        xanchor = "right",
        x = 1
    ),
    xaxis = dict(
        showgrid = True,
        showline = False,
        showticklabels = False
    ),
    yaxis = dict(
        showgrid = True,
        showline = False,
        showticklabels = True
    )
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/50.png")