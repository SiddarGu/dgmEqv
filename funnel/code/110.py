

import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [1000, 880, 666, 462, 228],
    textinfo = "value+percent initial",
    marker_color = "dodgerblue",
    opacity = 0.7,
    connector = {"line":{"color":"royalblue"}},
))

fig.update_layout(
    title = {
        'text': "Financing Scenario for Business in 2021",
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font = {
        "family": "Courier New, monospace",
        "size": 14,
        "color": "#7f7f7f"
    },
    legend = {"x":0.8, "y":0.8},
    hovermode = "closest",
    xaxis_title = "Number of Investors",
    height = 800,
    width = 1200,
    paper_bgcolor = "#e2e2e2",
    plot_bgcolor = "#e2e2e2",
    showlegend = True
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/49.png")