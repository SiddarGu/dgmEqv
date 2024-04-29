
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Engagement", "Followers", "Likes", "Shares", "Comments", "Other"],
    x = [100000, 80000, 60000, 40000, 20000, 10000],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.75,
    marker = {"color": ["royalblue", "darkorange", "limegreen", "orangered", "darkviolet", "slategray"]}
))

fig.update_layout(
    title = {"text": "Social Media and the Web - User Engagement in 2021", "font": {"size": 24, "family": "Arial"}},
    font = {"family": "Arial"},
    autosize = False,
    width = 800,
    height = 600
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/17.png")