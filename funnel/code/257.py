
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Pre-Game Activities","Ticket Sales","In-Game Activities","Post-Game Activities","Merchandise Sales"],
    x = [5000, 4000, 3000, 2000, 1000],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.7,
    marker = dict(
        color = ["rgb(0,255,0)","rgb(255,0,0)","rgb(0,0,255)","rgb(255,255,0)","rgb(255,0,255)"]
    )
))

fig.update_layout(
    title = {
        'text':"Sports and Entertainment Events Attendance in 2020",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font = dict(
        size=14,
        color="#000000"),
    legend = dict(
        orientation="h",
        xanchor="center",
        yanchor="bottom",
        y=1.02,
        x=0.5
    ),
    xaxis = dict(
        showgrid = True,
        gridcolor = 'rgb(232,232,232)',
        zeroline = True,
        zerolinecolor = 'rgb(232,232,232)',
        showline = True,
        linewidth = 1
    ),
    yaxis = dict(
        showgrid = True,
        gridcolor = 'rgb(232,232,232)',
        zeroline = True,
        zerolinecolor = 'rgb(232,232,232)',
        showline = True,
        linewidth = 1
    ),
    margin = dict(t=20, b=20, l=20, r=20),
    paper_bgcolor='#FFFFFF',
    plot_bgcolor='#FFFFFF',
    width=800,
    height=600,
    showlegend=True
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/107.png")