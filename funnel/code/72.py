
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Search", "Engagement", "Conversion", "Retention", "Advocacy"],
    x = [1000, 800, 600, 400, 200],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["#f5f5f5", "#e7e7e7", "#d9d9d9", "#cccccc", "#bebebe"]}
))
fig.update_layout(
    title_text = "Technology and the Internet - User Funnel in 2020",
    width = 800,
    height = 700,
    showlegend = False
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/93.png")