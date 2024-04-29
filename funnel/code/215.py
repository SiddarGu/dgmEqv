
import plotly.graph_objects as go

data = [go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [200000, 160000, 120000, 80000, 40000, 32000],
    textinfo = "value+percent initial",
    marker = {'color': ['#f5f5f5', '#e9e9e9', '#dcdcdc', '#bfbfbf', '#a6a6a6', '#8c8c8c']},
    textposition = "inside",
    opacity = 0.8,
    orientation = "h"
    )]

fig = go.Figure(data)
fig.update_layout(
    title = "Social Media and Web Usage in 2021",
    font = dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"),
    plot_bgcolor='rgba(0,0,0,0)',
    showlegend=True,
    legend_orientation="h",
    legend=dict(x=0, y=-0.15),
    margin=dict(l=20, r=20, t=35, b=20),
    width=800,
    height=400,
    paper_bgcolor='rgba(0,0,0,0)',
    hovermode='x',
    dragmode=False
    )

fig.write_image("../png/215.png")