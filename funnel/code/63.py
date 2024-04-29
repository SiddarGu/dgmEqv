
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry","Feasibility Study","Project Planning","Implementation","Operation"],
    x = [1000,900,700,500,300],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker = {"color": ["royalblue","crimson","orange","lightseagreen","mediumturquoise"]},
))
fig.update_layout(title_text="Energy and Utilities Consumer Growth in 2021",margin=dict(t=50, l=50, r=50, b=50),
    font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    width=800,
    height=650,
    showlegend=True,
    legend=dict(
        x=0.8,
        y=0.7,
    ))
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/84.png")