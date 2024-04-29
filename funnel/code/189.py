
import plotly.graph_objects as go
import plotly.io as pio

data = [go.Funnel(
    y = ['Initial Inquiry', 'Feasibility Study', 'Project Planning', 'Implementation', 'Operation'],
    x = [200, 176, 132, 88, 44],
    textinfo = 'value+percent initial',
    textposition = 'inside',
    marker_color = 'dodgerblue'
)]

fig = go.Figure(data)
fig.update_layout(
    title = {
        'text': 'Healthcare and Health Services in 2020',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    font = dict(family='Courier New', size=14),
    width = 800,
    height = 600
)

fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/3.png')