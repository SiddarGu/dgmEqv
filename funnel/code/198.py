
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Initial Interest", "Research", "Consideration", "Intent", "Purchase", "Follow-up"],
    x = [1000, 800, 600, 400, 200, 150],
    textinfo = "value+percent initial",
    textposition = "outside",
    marker = dict(
        color = "royalblue",
        line = dict(
            color = "royalblue",
            width = 2
        )
    ),
    opacity = 0.75,
    connector = {"line":{"color":"royalblue","dash":"solid","width":2}}
))

fig.update_layout(
    title = {"text": "Customer Engagement in Sports and Entertainment in 2021",
             "x": 0.5,
             "y": 0.95,
             "xanchor": "center",
             "yanchor": "top"},
    font = dict(family="monospace"),
    paper_bgcolor = "white",
    plot_bgcolor = "white",
    margin = dict(t=50, b=50, l=50, r=50),
    width = 800,
    height = 800,
    hovermode = "closest",
    showlegend = True,
    legend_orientation = "h",
    legend_x = -0.05,
    legend_y = 1.1
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/109.png")