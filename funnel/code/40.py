
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Voter Registration", "Voter Awareness", "Voter Education", "Voter Turnout", "Voter Campaigns"],
    x = [5000, 4500, 4000, 3000, 2000],
    textinfo="value+percent initial",
    orientation="h"
))

fig.update_layout(
    title={"text": "Voter Engagement in Government and Public Policy in 2021", "x":0.5, "y": 0.95},
    legend_orientation="h",
    legend_y=-0.2,
    font=dict(family="Lato"),
    width=1000,
    height=800
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/14.png")