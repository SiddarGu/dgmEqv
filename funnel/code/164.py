
import plotly.graph_objects as go
import plotly.io as pio

data = [go.Funnel(
    y = ["Inquiry", "Research", "Planning", "Implementation", "Operation", "Others"],
    x = [1000, 800, 600, 400, 200, 150],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker_color = '#6699cc',
    opacity = 0.7
)]

fig = go.Figure(data)
fig.update_layout(
    title = "Manufacturing and Production in 2020",
    title_x = 0.5,
    font = {"family": "Times New Roman"},
    width = 800,
    height = 600,
    showlegend = True,
    legend_orientation = "h",
    legend = dict(x = 0, y = 1.2),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/168.png")