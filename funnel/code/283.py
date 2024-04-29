
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Development", "Approval", "Implementation", "Review", "Finalizing", "Archive"],
    x = [100, 90, 80, 70, 60, 50],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.7,
    marker = {'color': ['#f963e7', '#f9e3e7', '#f9cce7', '#f9b3e7', '#f99ce7', '#f986e7']},
    connector = {"line":{"color":"#f7c2d0", 
                    "dash":"dashdot",
                    "width":3}},
))

fig.update_layout(
    title =  "Government and Public Policy - Progress Analysis in 2021",
    font = dict(family="Calibri,monospace", size=14),
)

fig.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    autosize=True,
    width=1000,
    height=600,
    margin=dict(l=50, r=50, b=50, t=50, pad=4),
    legend_orientation="h",
    legend=dict(x=0.2, y=-0.2)
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/14.png")