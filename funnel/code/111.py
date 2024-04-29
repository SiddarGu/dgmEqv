
import plotly.graph_objects as go
import numpy as np

# Data
stage = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"]
number_of_referrals = [1000, 900, 800, 700, 600, 500]

# Funnel
fig = go.Figure(go.Funnel(
    y = stage,
    x = number_of_referrals,
    textinfo = "value+percent initial",
    opacity = 0.7,
    marker_color = np.random.randn(6),
    textposition = "inside",
))

# Layout
fig.update_layout(
    title = "Increasing Referrals in Sports and Entertainment in 2021",
    font = dict(
        family = "Courier New, monospace",
        size = 16,
        color = "RebeccaPurple"
    ),
    autosize = False,
    width = 800,
    height = 600,
    showlegend = True,
    legend_orientation="h",
    legend = dict(
        x = 0.5,
        y = -0.2
    ),
    xaxis_title="Number of Referrals",
    yaxis_title="Stage",
    paper_bgcolor = 'rgba(0,0,0,0)',
    plot_bgcolor = 'rgba(0,0,0,0)',
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/5.png")