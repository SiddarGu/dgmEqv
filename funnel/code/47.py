
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Searching", "Trial Sign up", "Subscription", "Renewal", "Advocates"],
    x = [10000, 7000, 3000, 1000, 500],
    textinfo = "value+percent initial",
    orientation = "h",
    marker = {"color": ["#333333", "#996699", "#CC99CC", "#FFCCFF", "#FFFFFF"]},
))

fig.update_layout(
    title_text = "User Engagement - Technology and the Internet in 2020",
    font = {"family": "sans serif"},
    showlegend = True,
    legend_orientation = "h",
    legend_x = 0,
    legend_y = 1.2,
    margin = dict(l=200, r=200, t=50, b=50)
)

fig.update_layout(
    width=1000,
    height=600,
    autosize=False,
    paper_bgcolor="LightSteelBlue",
)

pio.write_image(fig, '/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/21.png')