import plotly.graph_objects as go
import pandas as pd

# data
data = {'Date': ['2019-03-01', '2019-03-02', '2019-03-03', '2019-03-04', '2019-03-05'],
        'Open Price ($)': [45.5, 46, 46.5, 47, 48.5],
        'Close Price ($)': [46, 45.1, 47, 48.5, 49.8],
        'High Price ($)': [48.2, 47.2, 48, 49.7, 50.5],
        'Low Price ($)': [44.6, 44.7, 45, 46.5, 47.6]}

df = pd.DataFrame(data)

# create trace for candlestick chart
trace = go.Candlestick(x=df['Date'],
                       open=df['Open Price ($)'],
                       close=df['Close Price ($)'],
                       high=df['High Price ($)'],
                       low=df['Low Price ($)'])

# create layout
layout = go.Layout(title='March Financial Marketplace Review',
                   autosize=False,
                   width=800,
                   height=600,
                   yaxis_range=[min(df['Low Price ($)']) - 1, max(df['High Price ($)']) + 1],
                   margin=dict(l=50, r=50, t=50, b=50))

# create figure
fig = go.Figure(data=[trace], layout=layout)

# save figure as image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/228_202312302255.png')