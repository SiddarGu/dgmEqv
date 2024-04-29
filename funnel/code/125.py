
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Interest", "Enrollment", "Learning", "Completion", "Graduation"],
    x = [100, 88.8, 66.6, 46.2, 22.8], 
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.8,
    marker_color = 'darkgreen'
))

fig.update_layout(
    title = "Student Journey in Social Sciences and Humanities in 2021",
    font = dict(
        family = "Courier New, monospace",
        size = 14,
        color = "#7f7f7f"
    ),
    paper_bgcolor = "white",
    width = 800,
    height = 600,
    showlegend = False,
    margin = dict(
        l = 0,
        r = 0,
        t =50,
        b =0
    ),
    xaxis = dict(showgrid = True, zeroline = False),
    yaxis = dict(showgrid = True, zeroline = False)
)

fig.write_image("../png/78.png")