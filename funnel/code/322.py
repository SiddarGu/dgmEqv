
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Planting", "Growing", "Harvesting", "Processing", "Distribution"],
    x = [500, 400, 300, 200, 100],
    textinfo = "value+percent initial",
    textposition = "outside",
    marker_color = ["#f5da42", "#86cd82", "#5e9dbd", "#7f5a83", "#d08686"],
    opacity = 0.7,
    orientation = "h"
))
fig.update_layout(
    title_text = "Agriculture and Food Production - Growth in Farms in 2020",
    font_size = 12,
    legend_title_text = "Stage",
    legend_orientation = "h",
    legend_x = 0.05,
    legend_y = 0.9,
    width = 950,
    height = 600,
    paper_bgcolor = "rgba(0,0,0,0)",
    plot_bgcolor = "rgba(0,0,0,0)",
    showlegend=True,
    margin=dict(l=0, r=0, t=80, b=50)
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/45.png")