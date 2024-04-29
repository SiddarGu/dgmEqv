
import plotly.graph_objects as go
data = [go.Funnel(
    name = "Science and Engineering Projects Development in 2021",
    textinfo = "value+percent initial",
    opacity = 0.9,
    x = [100, 85, 60, 40, 20, 10],
    y = ["Research", "Design", "Development", "Testing", "Production", "Distribution"],
    marker_color = '#d35400'
)]

layout = go.Layout(title = "Science and Engineering Projects Development in 2021",
                   font = dict(family = 'Arial'),
                   showlegend=True,
                   legend=dict(x=0, y=1, orientation="h"),
                   grid = dict(rows=1, columns=1),
                   height = 700,
                   width = 700,
                   margin = dict(l=50, r=50, b=50, t=50, pad=4)
)

fig = go.Figure(data=data, layout=layout)
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.write_image("../png/25.png")