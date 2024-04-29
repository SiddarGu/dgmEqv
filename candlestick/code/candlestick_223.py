import plotly.graph_objects as go

# Create data
data = [['2020-01-01', 300, 305, 320, 290],
        ['2020-02-01', 305, 310, 325, 295],
        ['2020-03-01', 310, 315, 330, 300],
        ['2020-04-01', 315, 320, 335, 305],
        ['2020-05-01', 320, 325, 340, 310],
        ['2020-06-01', 325, 330, 345, 315],
        ['2020-07-01', 330, 335, 350, 320],
        ['2020-08-01', 335, 340, 355, 325],
        ['2020-09-01', 340, 345, 360, 330],
        ['2020-10-01', 345, 350, 365, 335],
        ['2020-11-01', 350, 355, 370, 340],
        ['2020-12-01', 355, 360, 375, 345]]

# Create figure and candlestick
fig = go.Figure(data=[go.Candlestick(x=[row[0] for row in data],
                                     open=[row[1] for row in data],
                                     close=[row[2] for row in data],
                                     high=[row[3] for row in data],
                                     low=[row[4] for row in data])])

# Set title
fig.update_layout(title="Monthly Real Estate Price Trend in 2020")

# Adjust layout
fig.update_layout(width=800, height=400)
fig.update_layout(autosize=False)
fig.update_layout(showlegend=False)
fig.update_yaxes(range=[min([row[4] for row in data])-10, max([row[3] for row in data])+10])
fig.update_layout(font=dict(family="Arial, sans-serif"))

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/102_202312302255.png')