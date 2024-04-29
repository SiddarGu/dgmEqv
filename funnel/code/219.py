
import plotly.graph_objects as go 
import plotly.io as pio

# Create figure
fig = go.Figure(go.Funnel(
    y = ["Research","Experimentation","Design","Development","Deployment","Evaluation"],
    x = [1000,800,600,400,200,100],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["royalblue","crimson","lightseagreen","orange","lightgray","violet"]}
))

# Set figure title
fig.update_layout(title_text="Scientific and Engineering Progress in 2021")

# Set figure size
fig.update_layout(
    autosize=False,
    width=800,
    height=600
)

# Write figure to file
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/82.png")