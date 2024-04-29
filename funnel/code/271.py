

import plotly.graph_objects as go
import plotly.io as pio

data = [go.Funnel(
    y = ["Promotion","Registration","Orientation","Course Selection","Learning","Evaluation"],
    x = [1000,800,600,400,200,100],
    textinfo = "value+percent initial",
    marker = {"color": ["#636EFA", "#EF553B", "#00CC96", "#AB63FA","#FFA15A","#FF6692"]},
    hoverinfo = "text+name",
    textposition = "inside",
    opacity = 0.7,
    connector = {"line":{"color":"rgb(63, 63, 63)"}}
)]

fig = go.Figure(data)

fig.update_layout(
    title = "Education Journey of Social Sciences and Humanities in 2021",
    font = {"family":"sans-serif"},
    paper_bgcolor = "rgba(0,0,0,0)",
    plot_bgcolor = "rgba(0,0,0,0)",
    legend_orientation = "h",
    legend = dict(x = 0.2, y = -0.3),
    width = 800,
    height = 800,
    margin = dict(l = 20, r = 20, t = 40, b = 20),
    shapes = [
        dict(
            type = "rect",
            x0 = 0,
            y0 = 0,
            x1 = 1,
            y1 = 1,
            line = dict(
                color = "rgba(0, 0, 0, 0)",
                width = 0
            )
        )
    ]
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/78.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/78.png")