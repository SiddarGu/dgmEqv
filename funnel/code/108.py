
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Interest", "Evaluation", "Purchase", "Follow-up", "Retention", "Others"],
    x = [3000, 2400, 1800, 1200, 600, 480],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont = dict(
    size = 20,
    color = "white"),
    marker = dict(
    color = ["#2D3A60", "#5D6F91", "#8C9AB4", "#A9B6D0", "#C7D1E5", "#E4EDFA"],
    line = dict(
    width = 2,
    color = "white")
    ),
    opacity = 0.8
))

fig.update_layout(
    title = {"text": "Sports and Entertainment Funnel in 2020", 
             "y": 0.9,
             "x": 0.5,
             "xanchor": "center",
             "yanchor": "top"
            },
    font = dict(size = 18, family = "Arial"),
    width = 800,
    height = 600,
    shapes=[dict(
        type="rect",
        x0=0,
        y0=0,
        x1=1,
        y1=1,
        line=dict(
            color="LightSteelBlue",
        ),
    )],
    showlegend = True,
    legend = dict(
    x = 0.8,
    y = 1,
    traceorder = "normal",
    font = dict(
    size = 16,
    color = "black"),
    bgcolor = "LightSteelBlue",
    bordercolor = "Black",
    borderwidth = 2
    ),
    template = "plotly_dark"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/13.png")