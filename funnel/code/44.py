
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Online Ads", "Website Visits", "Product Inquiries", "Cart Additions", "Purchases"],
    x = [1000, 800, 600, 400, 200],
    textinfo = "value+percent initial",
    orientation = "h",
    textfont = dict(size = 18),
    marker = dict(
        color = ["#ABE5A1", "#51AEC9", "#5BC0BE", "#FDE74C", "#9BC53D"],
        line = dict(width = 0.2)
    )
))

fig.update_layout(
    title = "Consumer Journey in the Food and Beverage Industry in 2021",
    legend = dict(x=1, y=0.5),
    width = 800,
    height = 600,
    showlegend = True
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/26.png")