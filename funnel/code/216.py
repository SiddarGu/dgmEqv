
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Research","Booking","Arrival","Stay","Departure"],
    x = [500,400,300,200,100],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont = dict(
        color = "white"
    )
))

fig.update_layout(
    title = "Tourism and Hospitality - Numbers of Tourists in 2020",
    titlefont = dict(
        size = 24
    ),
    width = 800,
    height = 800,
    margin=dict(
        l=50,
        r=50,
        b=20,
        t=60,
        pad=4
    ),
    font = dict(
        color = "black"
    ),
    paper_bgcolor = "white",
    plot_bgcolor = "white",
    showlegend = False
)

fig.write_image(r"/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/71.png")