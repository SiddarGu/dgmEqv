
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [100, 88.8, 66.6, 46.2, 22.8],
    textinfo = "value+percent initial",
    orientation = "h",
    marker = {"color": ["#2d7bf4", "#4da6ff", "#77bfff", "#a1d2ff", "#ccecff"]}
))
fig.update_layout(
    title_text = "Project Development in Energy Sector in 2023",
    font = {"family": "Arial", "size": 12},
    showlegend = False,
    margin = {"t":50, "l":50, "b":50, "r":50},
    width = 800,
    height = 500,
    paper_bgcolor = "rgba(0,0,0,0)",
    plot_bgcolor = "rgba(0,0,0,0)"
)
fig.write_image(r"/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/46.png")