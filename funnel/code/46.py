
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [100, 88.8, 66.6, 46.2, 22.8],
    textinfo = "value+percent initial",
    textposition="inside",
    orientation="h"
))

fig.update_layout(
    title_text="Project Development in Energy Sector in 2023",
    font=dict(family="sans-serif")
)
fig.update_layout(
    margin = dict(
        l = 0,
        r = 0,
        b = 0,
        t = 50,
        pad = 0
    ),
    showlegend=True
)
fig.update_layout(
    autosize=True,
    width=800,
    height=600,
    font=dict(family="Arial"),
    paper_bgcolor="LightSteelBlue",
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/7.png")