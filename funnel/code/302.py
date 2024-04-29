
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Enrollment", "Attending", "Completing Course", "Attaining Degree", "Continuing Education"],
    x = [1000, 880, 660, 462, 228],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.8,
    marker = dict(
        color = ['royalblue', 'seagreen', 'orange', 'violet', 'gold'],
    )
))

fig.update_layout(
    title = {
        'text': 'Academic Achievement - Social Sciences and Humanities in 2021',
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    autosize=False,
    width=600,
    height=500,
    paper_bgcolor="LightSteelBlue",
    font=dict(
        family="Times New Roman",
        size=14
    )
)

fig.update_layout(legend_orientation="h")

fig.write_image("../png/20.png")