
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Initial Research", "Considerations", "Plan Development", "Implementation", "Monitoring", "Evaluation"],
    x = [200, 150, 120, 90, 60, 30],
    textinfo = "value+percent initial", 
    marker_line_width = 2,
    marker = {"color": ["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A", "#19D3F3"]},
    opacity = 0.65,
    hoverinfo = 'text+name',
    text = ["200 Actions", "150 Actions", "120 Actions", "90 Actions", "60 Actions", "30 Actions"],
    name = "Sustainability Initiatives in Environment Sector in 2021"
))

fig.update_layout(
    title = {"text": "Sustainability Initiatives in Environment Sector in 2021", "y":0.95, "x":0.5, "xanchor": "center", "yanchor": "top"},
    font = dict(
        family = "Courier New, monospace",
        size = 12,
        color = "#7f7f7f"
    ),
    width = 800,
    height = 600,
    margin = {"l": 150, "r": 150, "t": 100, "b": 100},
    paper_bgcolor = "white",
    plot_bgcolor = "white",
    showlegend = True,
    legend_orientation = "h",
    legend = dict(x=0.5, y=-0.25),
    xaxis = {"visible": True},
    yaxis = {"visible": True},
)

fig.write_image("../png/268.png")