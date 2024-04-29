
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Research and Development", "Prototyping", "Testing", "Manufacturing", "Distribution"],
    x = [100, 88.8, 66.6, 46.2, 22.8],
    textposition = "inside",
    textinfo = "value+percent initial"
))

fig.update_layout(
    title = {"text":"Product Development in Science and Engineering in 2021", "x":0.5, "xanchor":"center"},
    font = {"family":"Verdana"},
    width = 800,
    height = 600
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/64.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/64.png")