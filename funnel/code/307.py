
import plotly.graph_objects as go
import plotly.io as pio

data = [go.Funnel(
    y = ['Enrollment', 'Attendance', 'Grades', 'Graduation', 'Completion'],
    x = [10000, 9000, 7000, 5000, 3000],
    textinfo = 'value+percent initial',
    marker_color = 'dodgerblue',
    opacity = 0.7,
    marker = dict(
        line = dict(
            color = '#000000',
            width = 2
        )
    )
)]

layout = go.Layout(
    title = 'Academic Achievements of Students in Education Sector in 2020',
    font = dict(
        family = 'Courier New, monospace',
        size = 14,
        color = '#7f7f7f'
    ),
    showlegend = False,
    paper_bgcolor = 'rgba(0,0,0,0)',
    plot_bgcolor = 'rgba(0,0,0,0)',
    xaxis = dict(
        showgrid = True,
        gridcolor = '#bdbdbd',
        gridwidth = 1,
        zeroline = False
    ),
    yaxis = dict(
        showgrid = True,
        gridcolor = '#bdbdbd',
        gridwidth = 1,
        zeroline = False
    ),
)

fig = go.Figure(data=data, layout=layout)

fig.update_layout(width=800, height=600)

fig.write_image("../png/1.png")