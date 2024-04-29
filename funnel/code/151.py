
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [80, 64, 48, 32, 16],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.8
))

fig.update_layout(
    title_text = "Legal Cases Management in 2020",
    font = dict(family = "Courier New, monospace", size = 18, color = "#7f7f7f"),
    width = 1000,
    height = 800,
    paper_bgcolor = "white",
    plot_bgcolor = "white",
    legend_orientation = "h",
    legend_x = 0,
    legend_y = -0.2,
    showlegend = True
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/145.png")