
import plotly.graph_objects as go

fig = go.Figure(data=[go.Funnel(
    y = ["Initial Access", "Initial Engagement", "Subsequent Usage", "Continuous Usage", "Increase Usage"],
    x = [1000, 888, 666, 462, 228],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {
        "color": ["royalblue", "crimson", "green", "lightseagreen", "orange"]
    }
)])

fig.update_layout(
    title = "Technology Adoption Among Internet Users in 2021",
    font = dict(family = 'Courier New'),
    width = 800,
    height = 600,
    showlegend = False,
    paper_bgcolor = 'rgba(0,0,0,0)',
    plot_bgcolor = 'rgba(0,0,0,0)',
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/93.png")