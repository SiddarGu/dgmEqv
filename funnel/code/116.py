
import plotly.graph_objects as go

data = [go.Funnel(
    y = ['Research','Development','Application','Presentation','Analysis','Other'],
    x = [500,400,300,200,100,80],
    textinfo = "value+percent initial",
    marker_color = '#FFB6C1',
    opacity = 0.7,
    marker = {'line': {'width': 2, 'color': '#FFB6C1'}},
    hovertemplate = "Stage: %{y}<br>Number of People: %{x}<extra></extra>")]

layout = go.Layout(
    title = {'text': 'Scientific and Engineering Development in 2021',},
    xaxis = {'title':'Number of People'},
    yaxis = {'title':'Stage'},
    margin=dict(l=100, r=100, t=100, b=100),
    legend_orientation="h",
    legend=dict(x=0.5, y=-0.15),
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"),
    width=800,
    height=600
)

fig = go.Figure(data = data, layout = layout)
fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/63.png')