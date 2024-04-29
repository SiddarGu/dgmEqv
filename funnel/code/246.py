

import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Design", "Development", "Testing", "Production", "Distribution"],
    x = [100, 88, 66, 44, 22],
    textinfo = "value+percent initial",
    marker = {"color": ["dodgerblue", "royalblue", "mediumblue", "darkslateblue", "mediumslateblue"]},
    textposition = "inside",
    opacity = 0.65
))

fig.update_layout(
    title={
        'text': "Manufacturing and Production in 2020",
        'y':0.96,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
        family='Helvetica',
        size=15),
    legend=dict(
        x=0.6,
        y=1
    ),
    width=750,
    height=550,
    margin=dict(
        l=10,
        r=10,
        b=10,
        t=10,
    ),
    plot_bgcolor='#FFF',
    paper_bgcolor='#FFF',
    shapes=[
        dict(
            type="rect",
            x0=0,
            y0=0,
            x1=1,
            y1=1,
            line_color="LightSteelBlue"
        )],
    xaxis=dict(
        showgrid=True,
        gridcolor='LightSteelBlue',
        zeroline=False
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='LightSteelBlue',
        zeroline=False
    )
)

fig.write_image("../png/38.png")