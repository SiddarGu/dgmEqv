
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Research", "Subscription", "Trial", "Payment", "Retention"],
    x = [1000, 800, 600, 400, 200],
    textinfo = "value+percent initial",
    textfont_size = 10,
    textposition = "outside",
    opacity = 0.7,
    marker = {"color": ["#FFC000", "#FFA000", "#FF8000", "#FF6000", "#FF4000"]},
    connector = {"line":{"color":"rgb(63, 63, 63)"}}
))

fig.update_layout(
    title = {"text": "Increasing Adoption of Technology and the Internet in 2020", "y": 0.95, "x": 0.5, "xanchor": "center", "yanchor": "top"},
    font = dict(family="Arial, sans-serif"),
    width = 800,
    height = 600,
    showlegend = False
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/18.png")
#pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/18.png")