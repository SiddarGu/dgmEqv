
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Shipping", "Processing", "Distribution", "Delivery", "Customer Service"],
    x = [1000, 800, 600, 400, 200],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker = dict(
        color = ["royalblue", "crimson", "lightseagreen", "orange", "lightgrey"],
        line = dict(
            color = "black",
            width = 2
        )
    ),
    opacity = 0.7
))

fig.update_layout(
    title = "Logistical Management - Transportation and Logistics in 2021",
    font = dict(
        family = "Helvetica, monospace",
        size = 12,
        color = "black"
    ),
    paper_bgcolor = "white",
    plot_bgcolor = "white",
    autosize = True,
    width = 500,
    height = 650,
    showlegend = True,
    legend_orientation = "v",
    margin = dict(
        b = 0,
        l = 0,
        r = 0,
        t = 70
    )
)

fig.write_image("../png/36.png")
pio.write_image(fig, "../png/36.png")