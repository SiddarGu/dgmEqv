
import plotly.graph_objects as go
import plotly.io as pio
fig = go.Figure(go.Funnel(
    y = ["Sign Up", "Trial Usage", "Payment Confirmation", "Net Promoter Score", "Retention Rate"],
    x = [1000,800,600,400,200],
    textinfo = "value+percent initial",
    orientation = "h",
    textposition = "inside",
    opacity = 0.7
))
fig.update_layout(title = "User Engagement in Tech and Internet Industries in 2021",
                  font = dict(family = "Times New Roman"),
                  width = 800,
                  height = 500,
                  showlegend = False)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/34.png")
#pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/34.png")