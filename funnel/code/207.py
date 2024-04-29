
import plotly.graph_objects as go
import plotly.io as pio

data = [{'Stage': 'Research', 'Number of Users': 5000},
        {'Stage': 'Comparison', 'Number of Users': 3500},
        {'Stage': 'Purchase', 'Number of Users': 2000},
        {'Stage': 'Download', 'Number of Users': 1500},
        {'Stage': 'Usage', 'Number of Users': 1000},
        {'Stage': 'Retention', 'Number of Users': 250}]

fig = go.Figure()
fig.add_trace(go.Funnel(
    y=[stage['Stage'] for stage in data],
    x=[stage['Number of Users'] for stage in data],
    textinfo="value+percent initial",
    textposition="outside",
    opacity=0.9,
    marker_color='royalblue'
))
fig.update_layout(
    title={
        'text': "Technology and the Internet Usage in 2020",
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(family='Courier New, monospace', size=13, color='rgb(0,0,0)'),
    xaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
        gridwidth=1,
        linecolor='black',
        linewidth=1
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
        gridwidth=1,
        linecolor='black',
        linewidth=1
    ),
    showlegend=False,
    width=900,
    height=600,
    margin=dict(l=20, r=20, t=50, b=20)
)
fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/50.png')
pio.write_image(fig, '/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/50.png')