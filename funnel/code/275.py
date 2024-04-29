
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y = ["Website Visit", "Engagement", "Interaction", "Retention", "Conversion", "Others"],
    x = [20000, 18000, 16000, 14000, 12000, 10000],
    textinfo = "value+percent initial",
    marker_color = 'gold',
    textposition = "inside",
    opacity=0.7
)])

fig.update_layout(
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    title={
        'text': "Web Traffic Funnel in Social Media and the Web in 2021",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
        showline=True,
        linecolor='black',
        showticklabels=True,
        tickcolor='lightgray',
        ticks='outside',
        zeroline=True,
        zerolinecolor='black'
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
        showline=True,
        linecolor='black',
        showticklabels=True,
        tickcolor='lightgray',
        ticks='outside',
        zeroline=True,
        zerolinecolor='black'
    ),
    legend=dict(
        yanchor="top",
        y=1.02,
        xanchor="left",
        x=1
    ),
    width=1000,
    height=800,
    margin=dict(
        l=100,
        r=100,
        b=100,
        t=100,
        pad=4
    ),
)

pio.write_image(fig, "../png/134.png")