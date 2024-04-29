
import plotly.graph_objects as go
fig = go.Figure(data=[go.Funnel(
    y=["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x=[1000, 800, 600, 400, 200, 160], textinfo="value+percent initial",
    marker = dict(
        color = ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A", "#19D3F3"],
    ),
    opacity = 0.7
)])

fig.update_layout(
    title="Impact of Government Policies on Public Engagement in 2020",
    showlegend=True,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        family="Courier New, monospace",
        size=16
    ),
    legend = dict(
        orientation="h"
    ),
    width=1000,
    height=1000,
    margin=dict(
        l=50,
        r=50,
        b=150,
        t=50,
        pad=4
    ),
    xaxis = dict(
        showgrid = False
    ),
    yaxis = dict(
        showgrid = False
    )
)

fig.write_image("../png/119.png")