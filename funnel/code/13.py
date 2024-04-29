
import plotly.graph_objects as go
data = [go.Funnel(textinfo="value", orientation="h", 
    y=[ 'Research','Discussion','Drafting','Review','Publication','Amendments'], 
    x=[90, 72, 54, 42, 30, 18], marker_color = 'darkblue')]

fig = go.Figure(data)
fig.update_layout(title_text="Government Policy Development in 2021",
    font=dict(family="Verdana, monospace", size=12, color="black"),
    width=850, height=600,
    xaxis_title="Number of Policies", showlegend=False)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/22.png")