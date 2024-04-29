
import plotly.graph_objects as go
import plotly.io as pio

#Create data
data = {
    'Stage': ['Research','Development','Testing','Production','Promotion'],
    'Number of Projects': [100.0,80.8,64.6,51.7,40.5]
}

#Create figure
fig = go.Figure()
fig.add_trace(go.Funnel(
    y = data['Stage'],
    x = data['Number of Projects'],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.7
))

fig.update_layout(
    title = "Project Advancement in Science and Engineering in 2021",
    font = dict(family = "Courier New, monospace"),
    showlegend = False,
    grid = dict(rows = 1, columns = 1),
    margin = dict(l = 10, r = 10, t = 50, b = 10),
    width = 600,
    height = 600
)

#Save as png
pio.write_image(fig, '../png/45.png', width = 600, height = 600)