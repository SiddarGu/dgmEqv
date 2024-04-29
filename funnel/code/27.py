
import plotly.graph_objects as go

fig = go.Figure(data=[go.Funnel(
    y = ["Research Interests", "Literature Review", "Data Collection", "Analysis and Interpretation", "Conclusion"],
    x = [1000, 800, 600, 400, 200],
    textinfo = "value+percent initial",
    textposition = "inside",
    orientation = "h"
)
])

fig.update_layout(
    title = "Academic Progress in Social Sciences and Humanities in 2021",
    font = dict(
        family = "Times New Roman"
    ),
    width = 800,
    height = 600,
    showlegend = False
)

fig.write_image("../png/27.png")