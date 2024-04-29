
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [20000, 15000, 10000, 7500, 5000, 3000],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker = {"color": ["#FF7F0E", "#D62728", "#2CA02C", "#1F77B4", "#8C564B", "#9467BD"]}
))

fig.update_layout(
    title = {"text": "Green Initiative - Environment and Sustainability in 2021", "x": 0.5},
    font = {"family": "sans-serif"},
    legend = {"x": 0.1, "y": 0.7},
    width = 800,
    height = 900,
    xaxis = {"showgrid": True},
    yaxis = {"showgrid": True}
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/12.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/12.png")