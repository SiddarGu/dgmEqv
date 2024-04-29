
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Online Booking", "Payment confirm", "Ticket delivery", "Ticket claimed", "Ticket used"],
    x = [1000, 800, 700, 400, 200],
    textinfo = "value",
    orientation = "h"
))

fig.update_layout(
    title = "Ticketing System in Sports and Entertainment Industry in 2021",
    font = dict(family="Courier New, monospace", size=10, color="#7f7f7f"),
    showlegend = False
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/13.png")