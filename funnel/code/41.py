
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Discovery","Information search","Checkout","Payment","Delivery"],
    x = [1000, 300, 150, 50, 30],
    textinfo="value+percent initial",  # set textinfo to "value" or "value+percent initial"
    textposition="inside",
    orientation="h",
))
fig.update_layout(title_text="Purchasing Process - Food and Beverage Industry in 2020", font=dict(family="Courier New, monospace", size=14))
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#e0e0e0')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#e0e0e0')
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/47.png", width=900, height=600, scale=2)
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/47.png")