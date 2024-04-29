
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Funnel(
    y = ["Enrollment", "Orientation", "Participation", "Retention", "Graduation", "Follow-up"],
    x = [1000, 900, 800, 700, 400, 200],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker = {"color": ["deepskyblue", "royalblue", "slateblue", "mediumblue", "dodgerblue", "blue"]},
    opacity = 0.7,
    connector = {"line":{"color":"royalblue", "dash":"solid"}}
))

fig.update_layout(
    title = {"text": "Student Development in Social Sciences and Humanities in 2021", "y":0.9, "x":0.5, "xanchor": "center", "yanchor": "top"},
    xaxis_title = "Number of Students",
    yaxis_title = "Stage",
    width = 800,
    height = 600,
    legend_orientation="h",
    showlegend = True
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/43.png")