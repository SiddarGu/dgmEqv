
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y = ['Initial Assessment', 'Diagnosis', 'Treatment', 'Follow-up', 'Recovery'],
    x = [1000, 800, 600, 400, 200],
    textinfo = "value+percent initial",
    marker_color='#83bff6',
    opacity=0.6,
    connector = {'line': {'color': '#83bff6', 'dash': 'dot', 'width':2}},
)])

fig.update_layout(
    title={
        'text': "Patient Care in Healthcare and Health in 2021",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
        family="Arial",
        size=11,
        color='#7f7f7f'
    ),
    showlegend=True,
    legend_orientation="h",
    legend=dict(
        x=0.5,
        y=1.1
    ),
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
    height=600,
    width=800,
    margin=dict(
        l=10,
        r=10,
        b=10,
        t=50,
        pad=4
    ),
    xaxis_showgrid=True,
    yaxis_showgrid=True, 
    xaxis_zeroline=False,
    yaxis_zeroline=False
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/42.png")