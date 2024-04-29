
import plotly.graph_objects as go 
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Discovery","Evaluation","Purchase Decision","Payment","Delivery","Retention"],
    x = [1000,800,600,400,200,100],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker = dict(
        color = ["#a5c8e6", "#90caf9", "#64b5f6", "#42a5f5", "#1e88e5", "#1976d2"]
    ),
    opacity = 0.7,
    connector = {"line":{"color":"rgba(63, 63, 63, 0.5)"}},
))

fig.update_layout(
    title_text = "Customer Journey in Retail and E-commerce in 2021",
    font = dict(
        family = "Courier New, monospace",
        size = 18,
        color = "#7f7f7f"
    ),
    legend_orientation = "h",
    legend = dict(x = 0, y = -0.2),
    plot_bgcolor = "#fafafa",
    paper_bgcolor = "#fafafa",
    width = 1000,
    height = 700,
    margin = dict(t = 120),
    showlegend = True
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/95.png")