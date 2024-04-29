
import plotly.graph_objects as go
import plotly.io as pio

values = [1000, 800, 500, 300, 200, 100]
stages = ['Intake', 'Review', 'Investigation', 'Negotiation', 'Resolution', 'Dismissal']

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = stages,
    x = values,
    textinfo = "value+percent initial",
    marker_color='royalblue',
    opacity=0.8,
))

fig.update_layout(
    title={
        'text': "Legal Cases Resolved in Law and Legal Affairs in 2020",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    font=dict(family='Courier New, monospace',
              size=14,
              color='#7f7f7f'),
    width=800,
    height=600,
    showlegend=True,
    legend=dict(x=0.8, y=1),
    margin=go.layout.Margin(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hovermode='x',
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/86.png")