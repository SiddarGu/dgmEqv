
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Research and Development", "Designing", "Testing", "Manufacturing", "Delivery"],
    x = [100, 80, 60, 40, 20],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker_color="darkblue",
    opacity=0.7,
    orientation = "h"
))
fig.update_layout(title_text="Production Process in Manufacturing Industry in 2021",
    font=dict(
        family="Arial",
        size=20,
    ),
    margin=dict(l=200, r=50, t=100, b=100),
    width=1000,
    height=600
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/9.png")