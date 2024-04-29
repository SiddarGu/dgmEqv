import pandas as pd
import plotly.graph_objects as go

data = {'Date': ['2021-07-12', '2021-07-19', '2021-07-26', '2021-08-02', '2021-08-09', '2021-08-16', '2021-08-23', '2021-08-30', '2021-09-06', '2021-09-13', '2021-09-20'],
        'Open Price ($)': [120.5, 121, 124, 126.5, 127, 131, 136, 140, 142, 145, 148],
        'Close Price ($)': [122.3, 123, 126.2, 127.3, 130, 135, 139, 141, 144, 147, 149],
        'High Price ($)': [125.1, 125.7, 128.5, 130.1, 133, 138, 142, 145, 148, 151, 153],
        'Low Price ($)': [117.9, 119.6, 121.5, 124.8, 125.7, 127.1, 132, 136.5, 138.6, 141, 143.8]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

fig.update_layout(
    title='E-commerce Platform Stock Trend Over Three Months',
    xaxis_title='Date',
    yaxis_title='Price ($)',
    width=800,
    height=600,
    yaxis_range=[min(df['Low Price ($)']) - 5, max(df['High Price ($)']) + 5]
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/57_202312302255.png')