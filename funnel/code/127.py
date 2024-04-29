
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [1000, 800, 500, 400, 200],
    textinfo = "value+percent initial",
    textposition="inside",
    marker = dict(
        color = ["#000000", "#092c67", "#a1d6e2", "#f2d841", "#f29a3d"]
    )
)])

fig.update_layout(
    title = {
        'text': "Energy Usage Trend in 2023",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
        family="Times New Roman"
    ),
    width=800,
    height=1000,
    showlegend=False,
    xaxis_showgrid=True,
    yaxis_showgrid=True,
    margin = dict(
        l=70,
        r=70,
        b=70,
        t=160,
        pad=10
    ),
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/84.png")