
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Raw Materials", "Initial Production", "Quality Assurance", "Packaging", "Distribution", "Retail"],
    x = [100, 80, 60, 40, 20, 10],
    textinfo = "value+percent total",
    textposition = "inside",
    hoverinfo = "text",
))
fig.update_layout(title_text="Product Output in Manufacturing and Production in 2021",
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"))
fig.update_xaxes(title_text="Number of Products")
fig.update_yaxes(title_text="Stage")
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/67.png", width=1200, height=900, scale=2)