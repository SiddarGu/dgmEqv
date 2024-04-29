
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Market Analysis", "Financial Planning", "Risk Evaluation", "Investment", "Transaction"],
    x = [100, 88.8, 66.6, 46.2, 22.8],
    textinfo = "value+percent initial",
    orientation = "h"
))
fig.update_layout(
    title = {
        'text': "Financial Deals in Business and Finance 2020",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    font = dict(family = "Calibri"),
    legend = {
        'x': 0.5,
        'y': -0.15,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    width = 800,
    height = 400,
    margin = dict(l = 0, r = 0, t = 70, b = 30)
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/44.png")