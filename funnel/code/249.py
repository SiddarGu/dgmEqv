
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Research","Design","Testing","Production","Maintenance"],
    x = [100,87.5,75,60,45],
    textinfo = "value+percent initial",
    marker= {"color": ["blue","green","yellow","red","purple"]},
    opacity = 0.65,
    textposition="inside",
))

fig.update_layout(
    title="Advancement of Science and Engineering in 2021",
    font={'family': 'Courier New', 'size': 18},
    width=900,
    height=500,
    showlegend=True,
    legend=dict(
        x=0.5,
        y=-0.25,
        orientation="h",
    )
)
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/45.png")