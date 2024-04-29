
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Enrollment", "Selection", "Interviews", "Admission", "Orientation", "Graduation"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont = dict(
        size = 16
    )
))

fig.update_layout(
    title = {
        'text': 'Student Journey in Science and Engineering Programs in 2021',
        'y':0.90,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    font = dict(
        size = 16
    ),
    width = 800,
    height = 500,
    legend_title = "",
    showlegend = True,
    legend = dict(
        x = 0.85,
        y = 1.0
    )
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/82.png")