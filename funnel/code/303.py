
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [1000, 800, 600, 400, 200, 160],
    textinfo = "value+percent initial",
    textposition = "outside",
    marker = dict(
        line = dict(
            width = 3,
            color = "black"
        )
    )
))

fig.update_layout(
    title = "Customer Engagement in Technology and Internet in 2021",
    paper_bgcolor = "white",
    plot_bgcolor = "white",
    font = dict(
        color = "black",
        family = "Courier New, monospace"
    ),
    width = 800,
    height = 500,
    showlegend = True,
    legend_orientation = "h",
    legend = dict(
        x = 0.2,
        y = 1.1
    ),
    margin = dict(
        l = 10,
        r = 10,
        b = 10,
        t = 60
    )
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/21.png")