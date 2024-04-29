
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Research", "Drafting", "Approval", "Implementation", "Evaluation"],
    x=[100, 80, 60, 40, 20],
    textinfo = "value+percent initial",
    orientation = "h",
))
fig.update_layout(
    title = "Policy Development in Government and Public Policy in 2021"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/16.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/16.png")