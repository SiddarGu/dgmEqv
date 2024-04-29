
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Ads Impression", "Product Page View", "Added To Cart", "Checkout", "Purchase"],
    x = [1000, 800, 500, 400, 200],
    textinfo = "value+percent initial",
    orientation = "h",
    opacity = 0.8
))

fig.update_layout(
    title = "Online Shopping Funnel - Retail and E-Commerce in 2020",
    font = dict(family="Courier New, monospace", size=14),
    showlegend = True,
    legend_orientation="h",
    width=800,
    height=600,
    paper_bgcolor = "LightSteelBlue"
)

fig.write_image(
    "../png/30.png"
)
pio.write_image(fig,
    "../png/30.png"
)