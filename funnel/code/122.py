
import plotly.graph_objects as go 
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y=['Introduction', 'Research', 'Analysis', 'Application', 'Conclusion', 'Review'],
    x=[200, 160, 128, 96, 64, 32],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.8,
    marker = dict(
        color = ['#56C2FF', '#2D9AFF', '#0B72E1', '#064DAA', '#062F7B', '#021648'],
        line = dict(width = 2)
    )
)])

fig.update_layout(
    title = {
        'text': 'Academic Performance in Social Sciences and Humanities in 2020',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title="Number of Students",
    font=dict(
        family="sans-serif",
        size=12,
        color="black"
    ),
    showlegend = False,
    grid=dict(
        rows=1,
        columns=1,
        pattern='independent'
    ),
    margin=dict(
        l=50,
        r=50,
        t=50,
        b=50
    ),
    width=600,
    height=400,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    hovermode='x',
    legend_orientation="h"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/70.png")