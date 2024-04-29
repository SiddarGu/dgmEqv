
import plotly.graph_objs as go
import plotly.io as pio

data = [go.Funnel(
    y = ["Elementary School", "High School", "Undergraduate", "Graduate School", "Doctorate", "Post-Doctorate"],
    x = [50000, 40000, 30000, 20000, 10000, 5000],
    textinfo="value+percent initial",
    marker_color='deeppink',
    opacity=0.7,
    textfont_size=15,
    hoverinfo="y+x",
    textposition="inside"
)]

layout = go.Layout(
    title="Education Pipeline in Science and Engineering in 2021",
    font=dict(
        family="Courier New, monospace",
        size=18
    ),
    width=900,
    height=700,
    xaxis_title="Number of Students",
    xaxis_showgrid=True,
    yaxis_title="Stage",
    yaxis_showgrid=True,
    showlegend=False,
    margin=go.layout.Margin(
        l=50,
        r=50,
        b=50,
        t=50,
        pad=4
    )
)

fig = go.Figure(data=data, layout=layout)
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

fig.write_image("../png/63.png")
pio.write_image(fig, "../png/63.png")