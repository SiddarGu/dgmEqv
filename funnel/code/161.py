
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [20000, 15000, 10000, 7000, 3000, 2000],
    textinfo = "value+percent initial",
    marker = dict(
        color = ["royalblue", "crimson", "green", "darkorange", "lightseagreen", "violet"],
        line = dict(
            color = "white",
            width = 3
        )
    )
))

fig.update_layout(
    title =  "Public Perception of Government and Public Policy in 2019", 
    plot_bgcolor = 'white',
    font = dict(
        family = "serif",
        size = 12
    ),
    legend = dict(
        font = dict(
            size = 12
        ),
        x = 0,
        y = 1
    ),
    margin = dict(
        l = 0,
        r = 0,
        b = 0,
        t = 40,
        pad = 0
    ),
    showlegend = True,
    width = 600,
    height = 600,
    paper_bgcolor = 'white',
    grid = dict(
        rows = 1,
        columns = 1
    )
)

fig.write_image("../png/16.png")