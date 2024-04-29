

import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ['Interest','Consideration','Intent','Conversion','Post-Purchase'],
    x = [1000, 800, 600, 400, 200],
    textinfo = 'value+percent initial',
    orientation = 'h',
    marker_color = 'rgb(255, 140, 0)'
))

fig.update_layout(
    title = 'Customer Journey in Retail and E-commerce in 2021',
    title_x = 0.5,
    font = dict(
        family="Courier New, monospace",
        size=14,
        color="black"
    ),
    margin = dict(l=170, r=170, t=50, b=50),
    showlegend = False,
    hovermode = 'x unified',
    paper_bgcolor = 'white',
    plot_bgcolor = 'white'
)

fig.update_yaxes(showgrid = True, gridwidth = 1, gridcolor = '#cccccc')
fig.update_xaxes(showgrid = True, gridwidth = 1, gridcolor = '#cccccc', tickfont=dict(size=14))

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/108.png", width=800, height=600)