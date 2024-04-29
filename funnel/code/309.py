
import plotly.graph_objects as go
import plotly.io as pio

data = [
    {'Stage': 'Initial Inquiry', 'Number of Houses': 100},
    {'Stage': 'Feasibility Study', 'Number of Houses': 90},
    {'Stage': 'Project Planning', 'Number of Houses': 80},
    {'Stage': 'Implementation', 'Number of Houses': 70},
    {'Stage': 'Operation', 'Number of Houses': 60}
]

fig = go.Figure(data=[go.Funnel(
    textinfo="value+percent initial",
    y=[data[i]['Stage'] for i in range(len(data))],
    x=[data[i]['Number of Houses'] for i in range(len(data))],
    textposition='inside',
    textfont=dict(
        color='#000000',
        size=14
    ),
    marker=dict(
        color='#FF8C00',
        line=dict(
            color='#D3D3D3',
            width=1
        )
    )
)])

fig.update_layout(
    title={
        'text': 'Real Estate and Housing Market Overview in 2021',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    ),
    legend_orientation="h",
    legend=dict(x=0.5, y=-0.25),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    autosize=False,
    width=750,
    height=1000
)

fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/25.png')