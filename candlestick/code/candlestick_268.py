import plotly.graph_objects as go

# Creating candlestick trace
trace = go.Candlestick(x=['2019-04-01', '2019-04-02', '2019-04-03', '2019-04-04', '2019-04-05', '2019-04-06', '2019-04-07', '2019-04-08'],
                       open=[55, 57.5, 58, 62, 63, 65, 66.8, 67.9],
                       high=[58, 60.2, 62, 64, 66, 67.5, 69, 70],
                       low=[53.6, 55.2, 57.5, 59.5, 61.3, 62.2, 66, 67.1],
                       close=[57.2, 59, 60.5, 61.5, 64.2, 66.6, 67.5, 68.5])

# Creating layout
layout = go.Layout(title='Tourism and Hospitality Industry Stock Values Daily Range in April 2019',
                   width=800,
                   height=600,
                   xaxis=dict(tickfont=dict(size=8)),
                   yaxis=dict(range=[50, 75]))

# Creating figure object
fig = go.Figure(data=[trace], layout=layout)

# Saving figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/159_202312302255.png')