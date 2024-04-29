
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=1, specs=[[{"type": "funnel"}]])
fig.add_trace(go.Funnel(
    y=["Exposure", "Engagement", "Participation", "Investment", "Retention", "Advocacy"],
    x=[150, 125, 100, 75, 50, 25],
    textinfo="value+percent initial",
    marker_color="deepskyblue",
    textposition="inside"
))
fig.update_layout(
    title_text="Sports and Entertainment Engagement in 2020",
    font=dict(size=12, color="black"),
    legend_orientation="h",
    legend=dict(x=0.7, y=1),
    height=1000,
    width=1000,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=20, r=20, t=20, b=20)
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/40.png")