
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Homepage", "Category page", "Product page", "Payment page", "Checkout"],
    x = [100, 80, 60, 30, 10],
    textinfo = "value",
    orientation = "h",
    marker = {"color": ["#FFA500", "#FFE4B5", "#DDA0DD", "#EE82EE", "#FF0000"]},
))

fig.update_layout(
    title = "Shopping Funnel - Retail and E-commerce in 2021",
    font = {"size": 14, "family": "Arial"},
    paper_bgcolor = "#f7f7f7",
    plot_bgcolor = "#f7f7f7",
    legend_title_text = "",
    legend_orientation = "h",
    legend_yanchor = "bottom",
    legend_y = 0.1,    
    legend_x = 0.5,
    legend_xanchor = "center",
    margin = {"t": 40, "b": 30, "l": 20, "r": 20},
    height = 500,
    width = 700,
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/4.png")