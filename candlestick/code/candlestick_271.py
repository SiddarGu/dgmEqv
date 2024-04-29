import plotly.graph_objects as go
import pandas as pd

data = {
    'Date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01'],
    'Opening Price ($)': [75.2, 80, 83, 89, 88, 92],
    'Closing Price ($)': [77.6, 81.5, 85.7, 87.5, 89.5, 94],
    'High Price ($)': [80.9, 84.6, 88.9, 90.6, 93.1, 97],
    'Low Price ($)': [74.1, 78.5, 82.4, 85.5, 87.5, 90.5]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Opening Price ($)'],
    close=df['Closing Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)']
)])

fig.update_layout(
    title='Investment in Art Market: Semi-Annual Overview',
    xaxis=dict(title='Date'),
    yaxis=dict(title='Price ($)'),
    height=600,
    width=900
)

fig.update_yaxes(range=[70, 100])

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/106_202312302255.png')
