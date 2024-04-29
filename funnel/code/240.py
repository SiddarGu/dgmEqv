
import plotly.graph_objects as go
import plotly.io as pio

data = [
    go.Funnel(
        y = ["Initial Awareness", "Interest", "Consideration", "Intent", "Conversion", "Retention"],
        x = [1000, 800, 600, 400, 200, 100],
        textinfo = "value+percent initial",
        marker = dict(color = ["#2FA8F7", "#78D2F7", "#C5F0F9", "#F2F9FD", "#F7FDFD", "#FCFCFC"]),
        opacity = 0.8
    )
]

fig = go.Figure(data = data)

fig.update_layout(
    title = dict(text = "Engagement Funnel for Social Media and Web Platforms in 2021", x = 0.5, font = dict(family = "Cambria")),
    font = dict(family = "Cambria"),
    legend = dict(x = 0.1, y = 0.95, bgcolor = "rgba(255, 255, 255, 0.5)", font = dict(family = "Cambria", size = 10)),
    plot_bgcolor = "white",
    paper_bgcolor = "white",
    width = 800,
    height = 600,
    margin = dict(t = 100, l = 20, b = 20, r = 10),
    showlegend = False
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/24.png")