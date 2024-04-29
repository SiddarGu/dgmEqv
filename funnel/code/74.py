
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [100, 90, 80, 60, 40],
    textinfo = "value+percent initial"))

fig.update_layout(
    title = "Project Development in Energy Sector in 2021",
    showlegend = False,
    font = dict(family = "Courier New"),
    plot_bgcolor =  '#cbd2d3',
    paper_bgcolor = '#cbd2d3',
    width = 800,
    height = 800
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/1.png")