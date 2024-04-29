
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Cultivation", "Harvesting", "Processing", "Packaging", "Distribution"],
    x = [100, 88.8, 66.6, 46.2, 22.8],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.75,
    marker = {"color": ["#fac1b7", "#a9bb95", "#92d8d8", "#e2a3c8", "#8cd3c5"]},
))

fig.update_layout(
    title = {"text": "Agri-Food Chain in 2021", "font": {"size": 20}},
    font = {"family": "Courier New, monospace", "size": 16},
    paper_bgcolor = "#f2f2f2",
    plot_bgcolor = "#f2f2f2",
    height = 600,
    width = 800,
    showlegend = False,
    margin={"l": 0, "r": 0, "b": 0, "t": 100},
)

fig.write_image("../png/15.png")