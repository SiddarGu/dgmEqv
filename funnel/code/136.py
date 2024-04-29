
import plotly.graph_objects as go
import plotly.io as pio

fig=go.Figure(go.Funnel(
    y=["Research","Development","Testing","Production","Distribution"],
    x=[1000,800,600,400,200],
    textinfo="value",
    textposition="inside",
    textfont_size=20,
    opacity=0.7,
    marker_color='#00b6cb',
    connector={"line":{"color":"#00b6cb","dash":"solid"}},
))

fig.update_layout(
    title={"text": "The Progress of Science and Engineering Projects in 2021", "y":0.9, "x":0.5, "xanchor": "center", "yanchor": "top"},
    font=dict(size=20,family="Courier New, monospace"),
    shapes=[dict(type="rect", xref="paper", yref="paper", x0=0, y0=0, x1=1, y1=1, line_width=2)],
    autosize=False,
    width=1000,
    height=800,
    margin=dict(
        l=100,
        r=100,
        b=100,
        t=100,
        pad=4
    ),
    showlegend=True,
    legend_orientation="h",
    legend=dict(x=0.2, y=1.2)
)

fig.write_image("../png/97.png")