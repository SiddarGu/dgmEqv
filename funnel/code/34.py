
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Purchase"],
    x = [1000, 800, 600, 400, 200],
    textinfo="value+percent initial",
    marker = {"color": ["#FFDB58", "#FFB300", "#FF8F00", "#FF6F00", "#FF3D00"]},
    opacity = 0.75,
    textposition = "inside"
))

fig.update_layout(
    title_text = "Customer Funnel in Retail and E-commerce in 2020",
    font = dict(
        family = "Times New Roman",
        size = 18,
        color = "#7f7f7f"
    ),
    width = 800,
    height = 500,
    showlegend = True,
    legend_orientation="h",
    margin = {"t":50},
    paper_bgcolor = "#f2f5fa"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/19.png")