
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Loading", "Transportation", "Delivery", "Unloading", "Receiving"],
    x = [1000, 800, 600, 400, 200],
    textinfo = "value+percent initial",
    orientation = "h",
    textposition = "inside",
))

fig.update_layout(
    title_text="Vehicle Movement in Transportation and Logistics in 2020",
    font=dict(family="Times New Roman"),
    showlegend=False,
    margin = dict(t=50, b=50, l=50, r=50),
    width = 800,
    height = 600,
    autosize=False,
)

pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/32.png")