
import plotly.graph_objects as go
import plotly.io as pio

data = [go.Funnel(
    y = ['Awareness', 'Interest', 'Consideration', 'Intent', 'Conversion', 'Others'],
    x = [1000, 800, 400, 200, 100, 80], 
    textposition = "inside",
    textinfo = "value+percent initial",
    opacity = 0.65,
    marker_color = 'rgb(63, 72, 204)')]

fig = go.Figure(data)
fig.update_layout(title = {
    'text': 'Donor Participation Trends in Charity and Nonprofit Organizations in 2020', 
    'x':0.5,
    'xanchor': 'center',
    'yanchor': 'top'}, 
    font = {'family':'Calibri'},
    legend_orientation="h",
    legend=dict(x=0, y=1.1),
    width = 1000,
    height = 800,
    margin=dict(l=20, r=20, t=40, b=20))

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/48.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/48.png")