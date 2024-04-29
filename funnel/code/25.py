
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion"],
    x = [20000, 15000, 10000, 5000, 1000],
    textinfo="value",
    orientation="h",
    marker_color='royalblue',
    textposition="inside"
))
fig.update_layout(
    title = {
        'text':"Growth of User Subscribers in Technology and Internet Industry in 2020",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
        family="Arial",
        color="#000000"
    ),
    legend_orientation="h",
    legend=dict(x=0.5, y=1.1),
    width=800,
    height=600,
    margin=dict(l=50, r=50, t=50, b=50),
    showlegend=True
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/18.png")