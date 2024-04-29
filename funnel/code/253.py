
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness","Interest","Consideration","Intent","Conversion","Others"],
    x = [500,400,300,200,100,80],
    textinfo="value+percent initial",
    textposition="inside",
    marker_line_color="darkslategray",
    marker_line_width=1.5,
    opacity=0.7,
    name="Donor Engagement - Charity and Nonprofit Organizations in 2020"
))

fig.update_layout(
    title = {"text":"Donor Engagement - Charity and Nonprofit Organizations in 2020","y":0.95,"x":0.5,'xanchor': 'center', 'yanchor': 'top'},
    font=dict(family="Arial", size=12, color="#000000"),
    showlegend = True,
    legend_orientation="h",
    legend=dict(x=0.5, y=-0.15),
    width=800,
    height=400,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, t=50, b=30)
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/128.png")