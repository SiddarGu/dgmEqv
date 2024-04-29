
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [200, 180, 144, 115.2, 57.6],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.65,
    marker_color='#0c3e9d',
))

fig.update_layout(
    title = "Tourism and Hospitality - Visitor Trends in 2021",
    font = dict(
        size=10
    ),
    width=1000,
    height=600,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/23.png")