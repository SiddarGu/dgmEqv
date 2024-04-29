
import plotly.graph_objects as go
import plotly.io as pio


fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.7,
    marker_color='royalblue'
))

fig.update_layout(
    title={"text": "Home Buyer Journey - Real Estate and Housing Market in 2020", "x":0.5},
    yaxis=dict(
        title="Stage"
    ),
    xaxis=dict(
        title="Number of Buyers"
    ),
    font=dict(
        family="Courier New, monospace", 
        size=12, 
        color="RebeccaPurple"
    ),
    width=800,
    height=600,
    legend_orientation="h",
    margin=dict(l=50, r=100, t=100, b=100),
    showlegend=True
)

fig.write_image("../png/41.png")