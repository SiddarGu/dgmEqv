

import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    name = 'Healthcare Journey of Patients in 2020',
    y = ["Pre-Screening", "Diagnosis", "Treatment", "Follow-up", "Discharge", "Aftercare"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    textposition = "outside",
    hoverlabel = dict(bordercolor = "black", bgcolor = "white"),
    marker = dict(
        color = ["#fcdeb2","#f7b2c8","#d2b2f7","#b2dffc","#b2f7d2","#e2f2b2"], 
        line = dict(
            color = "black",
            width = 1
        )
    )
))

fig.update_layout(
    title = "Healthcare Journey of Patients in 2020",
    height = 600,
    width = 800,
    font = dict(
        family = "Courier New, monospace",
        size = 12,
        color = "#7f7f7f"
    ),
    legend = dict(
        font = dict(
            family = "sans-serif",
            size = 12,
            color = "black"
        ),
        orientation = "h",
        yanchor = "bottom",
        y = 1.02,
        xanchor = "center",
        x = 0.5
    )
)

fig.update_xaxes(showgrid = True, gridwidth = 1, gridcolor = 'LightGray')
fig.update_yaxes(showgrid = True, gridwidth = 1, gridcolor = 'LightGray')

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/3.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/3.png")