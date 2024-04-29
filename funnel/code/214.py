
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Exploration", "Research", "Experimentation", "Development", "Innovation", "Production"],
    x = [200,170,140,105,80,60],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker_color = '#59a2d8',
    opacity = 0.9,
    textfont_size = 12
))

fig.update_layout(
    title = "Student Engagement in Science and Engineering in 2021",
    font = dict(
        size = 12
    ),
    legend=dict(
        x=0.9,
        y=1
    ),
    paper_bgcolor = '#f3f3f3',
    width = 550,
    height = 400,
    plot_bgcolor = '#f3f3f3',
    margin=dict(
        l=25,
        r=25,
        b=50,
        t=50
    )
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/64.png")