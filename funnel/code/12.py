
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Product Research", "Vendor Analysis", "Supplier Evaluation", "Pricing Comparison","Order Placement","Delivery"],
    x = [2500, 2000, 1600, 1100, 600, 400],
    textinfo = "value",
    textfont_size = 14,
    opacity = 0.8,
    marker = {"color": ["red", "royalblue", "green", "orange", "violet", "gold"]},
))

fig.update_layout(
    title = {"text": "Orders Fulfilled in Manufacturing and Production in 2021"},
    font = {"family": "Courier New, monospace", "size": 14},
    autosize = False,
    width = 800,
    height = 800,
    showlegend = True,
    xaxis_title = "Number of Orders",
    yaxis_title = "Stage",
    margin = {"l": 140, "b": 40, "t": 140, "r": 40},
    paper_bgcolor = "white",
    plot_bgcolor = "white",
    legend = {"x": 0.82, "y": 0.95},
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/9.png")