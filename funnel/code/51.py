
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Advertising","Online Ticketing","Booking Confirmation","Ticket Delivery","Payment Confirmation"],
    x = [20000,18000,15000,10000,5000],
    textinfo = "value+percent initial",
    orientation = "h",
    textfont_size = 14,
    opacity = 0.7
))

fig.update_layout(
    title_text = "Ticket Sale Funnel - Sports and Entertainment in 2021",
    font = dict(family="Courier New, monospace",
                size=12,
                color="RebeccaPurple"),
    xaxis = dict(
        showgrid = True,
        showline = True,
        showticklabels = True,
        gridcolor = 'rgb(255, 255, 255)',
        gridwidth = 1,
        zeroline = False
    ),
    yaxis = dict(
        showgrid = True,
        showline = True,
        showticklabels = True,
        gridcolor = 'rgb(255, 255, 255)',
        gridwidth = 1,
        zeroline = False
    ),
    paper_bgcolor='rgb(255, 255, 255)',
    plot_bgcolor='rgb(229, 229, 229)',
    width = 800,
    height = 800
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/5.png")