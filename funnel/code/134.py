
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Diagnosis", "Treatment", "Recovery", "Follow-Up", "Conclusion"],
    x = [1000, 830, 690, 510, 280],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker = {"color" : ["#2A9D8F", "#264653", "#E9C46A", "#F4A261", "#E76F51"]},
    opacity = 0.7
))

fig.update_layout(
    title = {"text" : "Healthcare and Health - Patient Journey in 2020", "x" : 0.5, "y" : 0.01},
    font = {"family" : "Times New Roman"},
    width = 600,
    height = 500,
    showlegend = False,
    paper_bgcolor = "#FFF5EE",
    margin = {"t" : 20, "b" : 0, "l" : 0, "r" : 0},
    xaxis = {"showgrid" : True, "showticklabels" : False},
    yaxis = {"showgrid" : False})

fig.write_image(r"../png/92.png")