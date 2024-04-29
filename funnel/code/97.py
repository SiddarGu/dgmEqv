
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [100, 75, 50, 25, 10],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.9,
    marker_color = '#2c7fb8'
)])

fig.update_layout(
    title = {
        'text': "Customer Engagement in Energy Sector in 2021",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font = dict(family="Times New Roman"),
    width = 800,
    height = 600,
    legend = dict(x=-0.1, y=1.1, traceorder="normal"),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/7.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/7.png")