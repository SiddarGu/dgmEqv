

import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Initial Inquiry","Feasibility Study","Project Planning","Implementation","Operation"],
    x = [1000,800,600,400,200],
    textinfo="value+percent initial",
    textposition="inside",
    marker = dict(
        color = "#00bcc2",
        line = dict(
            color = "#00bcc2",
            width = 3
        )
    )
))

fig.update_layout(
    title_text = "Healthcare Patient Journey in 2020",
    showlegend = False,
    paper_bgcolor = 'rgba(0,0,0,0)',
    plot_bgcolor = 'rgba(0,0,0,0)',
    font = dict(
        family = "Roboto"
    ),
    xaxis = dict(
        showgrid = True,
        gridcolor = "#e7e7e7"
    ),
    yaxis = dict(
        showgrid = True,
        gridcolor = "#e7e7e7"
    )
)

fig.update_yaxes(automargin=True)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/102.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/102.png")