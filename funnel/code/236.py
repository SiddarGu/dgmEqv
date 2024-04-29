
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Education", "Awareness", "Engagement", "Activation", "Adoption", "Others"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial"
))
fig.update_layout(
    title = "Environmental and Sustainability Awareness in 2020",
    paper_bgcolor = "white",
    font = dict(
        family = "Courier New, monospace",
        size = 12,
        color = "#7f7f7f"
    ),
    margin = dict(l=0, r=0, t=50, b=40),
    plot_bgcolor = "white"
)
fig.update_yaxes(
    showgrid = True,
    gridwidth = 1,
    gridcolor = "#dee2e6"
)
fig.write_image(r"../png/154.png")