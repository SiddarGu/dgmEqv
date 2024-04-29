
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Introduction", "Research", "Selection", "Implementation", "Maintenance", "Others"],
    x = [100000, 80000, 60000, 40000, 20000, 16000],
    textinfo = "value",
    textposition = "inside"
))

fig.update_layout(
    title = "Technology Adoption in the Internet - 2020",
    font = dict(
        family = "Courier New, monospace",
        size = 14,
        color = "#7f7f7f"
    )
)

fig.write_image("../png/60.png")
pio.write_image(fig, "../png/60.png")