
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Awareness", "Inquiry", "Application", "Admission", "Enrollment", "Graduation"],
    x = [2000, 1800, 1400, 1000, 800, 400],
    textinfo = "value+percent initial",
    marker = {"color": ["#f8d5cc", "#f5bcb5", "#f2a59e", "#ef8d88", "#ec7571", "#e95e5a"]},
    textposition = "inside",
    textfont_size = 15,
))

fig.update_layout(
    title = {
        'text': "Academic Progression in Education Sector in 2021",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font = {"size": 16},
    width = 1000,
    height = 800,
    showlegend = True,
    legend = {"x":0.85, "y":0.95},
    margin = {"l": 0, "r": 0, "b": 0, "t": 50},
    paper_bgcolor="LightSteelBlue",
    plot_bgcolor="LightSteelBlue",
)

fig.write_image("../png/23.png")