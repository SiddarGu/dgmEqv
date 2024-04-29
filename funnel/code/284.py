
import plotly.graph_objects as go
import pandas as pd

data = {'Stage': ['Initial Inquiry','Feasibility Study','Project Planning','Implementation','Operation'],
        'Number of Patients': [1000, 888, 666, 462, 228]}
df = pd.DataFrame(data)

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = df['Stage'],
    x = df['Number of Patients'],
    textinfo = "value+percent initial",
    textfont = dict(
        size = 12
    ),
    textposition = 'inside',
    opacity = 0.75,
    marker = dict(
        color = '#12C9E8',
        line = dict(
            color = '#2a6dff',
            width = 2
        )
    ),
    connector = dict(
        line = dict(
            color = '#2a6dff',
            width = 1
        )
    )
))

fig.update_layout(
    title = 'Patient Care in Healthcare and Health in 2020',
    font = dict(
        size = 14
    ),
    paper_bgcolor = '#f5f5f5',
    plot_bgcolor = '#f5f5f5',
    legend = dict(
        x = 0,
        y = 1
    ),
    width = 600,
    height = 400,
    xaxis = dict(
        showgrid = False,
    ),
    yaxis = dict(
        showgrid = False,
    )
)

fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/144.png', width=600, height=400, scale=2)