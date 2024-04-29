
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Research", "Inquiry", "Shortlist", "Offer", "Closing"],
    x = [1000, 800, 600, 400, 200],
    textinfo = "value+percent initial",
    textposition = "inside",
    hoverlabel = dict(bgcolor = "white", font_size = 16),
    marker = {"line": {"width": [1, 1, 1, 1, 1],
                  "color": ["#ededed", "#ededed", "#ededed", "#ededed", "#ededed"]}},
    opacity = 0.8
))

fig.update_layout(
    title = {"text": "House Purchases in Real Estate and Housing Market in 2020", 
             "x": 0.5, 
             "y": 0.95},
    font = dict(family = "Roboto"),
    legend = dict(yanchor="top", y=0.99,xanchor="left", x=0.01),
    width = 800,
    height = 500,
    margin = {"l":200, "r":200, "t":50, "b":50},
    paper_bgcolor = "#ededed",
    plot_bgcolor = "#ededed",
    yaxis = dict(categoryorder = "total descending"),
    shapes = [dict(type="rect", xref="paper", yref="paper", x0=0, y0=0, x1=1, y1=1, fillcolor="LightPink", opacity=0.5, layer="below")]
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/188.png")