
import plotly.graph_objects as go
import plotly.io as pio

values = [1000, 800, 600, 400, 200, 100]
phases = ['Research', 'Design', 'Development', 'Testing', 'Production', 'Maintenance']

fig = go.Figure(go.Funnel(
    y = phases,
    x = values,
    textinfo = "value+percent initial",
    opacity = 0.7,
    marker = dict(
        color = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3'],
    ),
    connector = {"line":{"color":"royalblue","dash":"solid","width":3}},
))

fig.update_layout(
    title =  "Science and Engineering Process in 2020",
    font = dict(size=11),
    legend = dict(x = 0.1, y = -0.2),
    margin=dict(l=20, r=20, t=45, b=15),
    # annotations = [{"text":"Source: Data.gov.uk","x": 0.1,"y": -0.2,"showarrow": False}],
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')

fig.update_layout(width=800, height=600)
fig.write_image("../png/227.png")