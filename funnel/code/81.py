
import plotly.graph_objects as go 
import plotly.express as px 

fig = go.Figure(go.Funnel(
    y = ["Analysis","Design","Planning","Production","Maintenance"],
    x = [100,80,60,40,20],
    textinfo = "value+percent initial",
    opacity = 0.5,
    marker = {"color": ["#EE8572", "#F7D794", "#8B9E9E", "#A3C9A8", "#8ED8F6"]}
))

fig.update_layout(
    title={
        'text': "Manufacturing and Production Process in 2020",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
        family="PingFang SC",
        size=14,
        color="black"
    ),
    legend_orientation="h",
    legend=dict(x=0.5, y=1.1),
    width = 800,
    height = 800,
    margin=dict(l=200, r=200, t=100, b=100),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    showlegend=True
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/28.png")