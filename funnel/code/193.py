
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness","Interest","Consideration","Intent","Conversion","Others"],
    x = [3000,2500,2000,1500,1000,800],
    textinfo = "value+percent initial",
    marker = {"color": ["#E84A5F", "#F1F2F6", "#ECECEC", "#FF5A5F", "#FFC857", "#A4C2F4"]},
    textposition = "inside",
    opacity = 0.8
    ))

fig.update_layout(
    title = {
        'text': "Consumer Journey for Technology and the Internet in 2021",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    font = {"family": "Courier New, monospace"},
    showlegend = True,
    legend_orientation="h",
    legend=dict(x=0, y=1.1),
    paper_bgcolor="LightSteelBlue",
    plot_bgcolor='rgba(0,0,0,0)',
    autosize=False,
    width=700,
    height=1000,
    margin=dict(
        l=10,
        r=10,
        b=100,
        t=100,
        pad=4
    ),
    annotations=[
    dict(
        x=0.5,
        y=1,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://www.example.com">example.com</a>',
        showarrow=False
    )
    ]
)

fig.write_image("../png/34.png")