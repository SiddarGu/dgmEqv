
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Research", "Inquiry", "Comparison", "Consideration", "Purchase","Retention"],
    x = [1000, 800, 650, 450, 200, 150],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.8,
    marker = {"color": ["#A836A8", "#A8A836", "#A8360C", "#36A8A8", "#366BA8", "#A8A8A8"]},
))

fig.update_layout(
    title = {"text": "Maximizing Customer Retention in Retail and E-commerce in 2021"},
    font = {"family": "Arial"},
    showlegend = True,
    legend_orientation = "h",
    legend_x = 0.4,
    legend_y = 1.05,
    margin = {"t": 50, "b": 10, "l": 10, "r": 10},
    width = 800,
    height = 600,
    paper_bgcolor = "white",
    plot_bgcolor = "white"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/4.png")