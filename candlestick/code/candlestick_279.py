import plotly.graph_objects as go
import pandas as pd

data = {
    'Date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01'],
    'Start Donation Amount ($)': [15000, 15200, 15500, 15800, 16000, 16300],
    'End Donation Amount ($)': [15200, 15400, 15700, 16000, 16200, 16500],
    'High Donation Amount ($)': [15600, 15800, 15900, 16200, 16400, 16700],
    'Low Donation Amount ($)': [14800, 15000, 15300, 15600, 15800, 16100]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Start Donation Amount ($)'],
    close=df['End Donation Amount ($)'],
    high=df['High Donation Amount ($)'],
    low=df['Low Donation Amount ($)'])
])

fig.update_layout(
    title='Monthly Donation Trends in Nonprofit Organizatio',
    width=800,
    height=600,
    yaxis=dict(range=[min(df['Low Donation Amount ($)']) * 0.9, max(df['High Donation Amount ($)']) * 1.1]),
    margin=dict(l=0, r=0, t=80, b=0)
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/172_202312302255.png')