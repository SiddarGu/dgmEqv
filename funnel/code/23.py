
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Registered","Verified","Engaged","Active","Loyal","Advocates"],
    x = [1000,900,800,700,600,500],
    textinfo = "value",
    orientation = "h"
))
fig.update_layout(
    title = {
        'text':"User Engagement on Social Media Platforms in 2020", 
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font = dict(
        family="Times New Roman"
    ),
    width=600,
    height=800,
    showlegend=False
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/24.png")