
import plotly.graph_objects as go

fig = go.Figure(data=[go.Funnel(
    y = ["Hiring","Interview","Training","Assigning Tasks","Evaluation"],
    x = [100,88.8,66.6,46.2,22.8],
    textinfo = "value",
    textposition = "inside",
    marker_color = '#FF7F50',
    opacity = 0.8)])

fig.update_layout(
    title = {'text':'Human Resources and Employee Management Process in 2021','x':0.5,'y':0.96},
    font_family = 'sans-serif',
    paper_bgcolor = 'rgba(0,0,0,0)',
    plot_bgcolor = 'rgba(0,0,0,0)',
    margin = {'t':30,'b':45},
    legend_orientation = "h",
    legend = dict(x = 0.5, y = 1.1),
    xaxis_title = 'Number of Employees',
    yaxis_title = 'Stage',
    yaxis = dict(tickmode = 'linear', tick0 = 0, dtick = 1),
    width = 500,
    height = 500,
    showlegend = False)

fig.write_image("../png/27.png")