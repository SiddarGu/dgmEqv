
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Funnel(
    y = ["Initial Consultation", "Investigation", "Research", "Action Plan", "Filing", "Disposition"],
    x = [100.0, 80.0, 60.0, 45.0, 30.0, 15.0],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.9,
    marker = {"color": ["#003366", "#0099cc", "#66ccff", "#b3e6ff", "#ccffff", "#ffffff"]},
    connector = {"line": {"color": "rgb(63, 63, 63)", "dash": "solid", "width": 2}}
))

fig.update_layout(
    title = {"text": "Legal Processes - Law and Legal Affairs in 2021",
             "x": 0.5,
             "y": 0.9,
             "xanchor": "center",
             "yanchor": "top"},
    font = {"size": 15},
    autosize = True,
    width = 900,
    height = 800,
    showlegend = False,
    xaxis = {"title": {"text": "Number of Cases"},
             "showgrid": True,
             "ticksuffix": "%",
             "showticklabels": True
            },
    yaxis = {"title": {"text": "Stage"},
             "showgrid": False,
            }
)

fig.write_image("../png/210.png")