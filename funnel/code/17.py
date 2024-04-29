
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Raw Material Acquisition","Tooling and Machining","Assembly","Testing and Quality Assurance","Shipping and Delivery"],
    x = [1000,800,600,400,200],
    textinfo = "value",
    textfont_size = 14,
    textposition = "inside",
    marker_color = 'rgb(255, 140, 0)'
))

fig.update_layout(
    title = "Manufacturing and Production Process in 2021",
    showlegend = False,
    height = 600,
    width = 800,
    margin=dict(l=0, r=0, t=50, b=0),
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/6.png")