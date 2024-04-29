
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y=["Awareness","Interest","Consideration","Intent","Conversion","Others"],
    x=[1000,800,600,400,200,150],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.7,
    marker_color='darkblue')])

fig.update_layout(
    title_text="Internet Usage in Technology Sector in 2021",
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
    showlegend=False,
    width=1000,
    height=600
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')

pio.write_image(fig, '/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/34.png')