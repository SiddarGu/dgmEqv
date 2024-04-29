
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [100, 80, 60, 40, 20],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["#FFCE56", "#FF8C00", "#FF6384", "#36A2EB", "#4BC0C0"]},
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
    showlegend = True
))
fig.update_layout(
    title = {
        'text': "Sustainable Project Development in Environment Sector in 2021",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    width=1000,
    height=650,
    xaxis = dict(
        gridcolor='rgb(255, 255, 255)',
        gridwidth=2,
        showgrid=True,
        zeroline=False,
        showline=False,
        ticks="outside",
        showticklabels=True
    ),
    yaxis = dict(
        gridcolor='rgb(255, 255, 255)',
        gridwidth=2,
        showgrid=True,
        zeroline=False,
        showline=False,
        ticks="outside",
        showticklabels=True
    )
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/36.png")