
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Interest","Consideration","Intent","Conversion","Others"],
    x = [1000,800,600,400,200],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont_size = 15,
    marker = {"color": ["#a6cee3", "#1f78b4", "#b2df8a", "#33a02c","#fb9a99"]},
    opacity = 0.7,
    orientation = "h"
))

fig.update_layout(
    title="Sports and Entertainment Engagement in 2021",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    width=800,
    height=500,
    xaxis = dict(
        showgrid = True,
        gridcolor = '#bdbdbd',
        gridwidth = 2
    ),
    yaxis = dict(
        showgrid = True,
        gridcolor = '#bdbdbd',
        gridwidth = 2
    ),
    legend_orientation="h"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/66.png")