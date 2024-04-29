
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Promotion", "Open House", "Interest", "Consideration", "Decision", "Purchase"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.9,
    hoverinfo = "y+x",
    marker_color = '#6d5cae'
))
fig.update_layout(
    title = "Visitor Engagement in Arts and Culture in 2021",
    font = dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    showlegend=False,
    width=600,
    height=800,
    margin=dict(l=20, r=20, t=50, b=20),
    paper_bgcolor="LightSteelBlue",
)

fig.write_image("../png/59.png")