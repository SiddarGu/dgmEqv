
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Awareness","Interest","Consideration","Intent","Conversion","Others"],
    x = [1000,800,600,400,200,160],
    textposition = "inside",
    textinfo = "value+percent initial",
    opacity = 0.7,
    marker_color = 'royalblue',
))

fig.update_layout(
    title = "User Engagement - Technology and the Internet in 2021",
    font = dict(family = 'Courier New, monospace', size = 16, color = '#7f7f7f'),
    showlegend = True,
    legend_orientation = "h",
    legend = dict(x = 0.5, y = 1.1),
    plot_bgcolor = 'white',
    paper_bgcolor = 'white',
    width = 1000,
    height = 700,
    margin = dict(l = 200, r = 200, t = 100, b = 200),
    xaxis = dict(showgrid = True, gridcolor = '#DDDDDD'),
    yaxis = dict(showgrid = True, gridcolor = '#DDDDDD'),
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/148.png")