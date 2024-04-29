
import plotly.graph_objects as go
fig = go.Figure(data=[go.Funnel(
    y=["Homepage", "Product Page", "Shopping Cart", "Checkout Page", "Payment Confirmation Page", "Others"],
    x=[1000, 800, 600, 400, 200, 100],
    textinfo="value",
    orientation="h"
)])
fig.update_layout(title_text="User Journey on Social Media and the Web in 2021")
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/17.png", scale=2, width=1600, height=800)