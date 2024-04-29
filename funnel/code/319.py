
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [500, 450, 400, 350, 300],
    textinfo="value+percent initial",
    textposition="inside",
    opacity = 0.8,
    marker = dict(
        color = ["royalblue", "crimson", "lightseagreen", "orange", "lightgrey"],
    ),
))

fig.update_layout(title_text="Real Estate Development in Housing Market in 2021",
                  font=dict(family="Courier New, monospace", size=18, color="black"),
                  width=1000, height=750,
                  legend_orientation="h",
                  legend=dict(x=0.7, y=1),
                  xaxis_showgrid=True,
                  yaxis_showgrid=True)

pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/40.png")