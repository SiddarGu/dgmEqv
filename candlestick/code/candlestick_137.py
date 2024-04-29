import pandas as pd
import plotly.graph_objects as go

data = {
    'Date': ['2020-10-12', '2020-10-19', '2020-10-26', '2020-11-02', '2020-11-09', '2020-11-16', '2020-11-23', '2020-11-30'],
    'Open Price ($)': [70, 73, 75.6, 73, 85.2, 75.6, 67, 63],
    'Close Price ($)': [72.8, 72, 73, 76, 78.1, 78.7, 65, 73],
    'High Price ($)': [74.1, 74, 76, 78, 85.2, 80.2, 68.9, 80.2],
    'Low Price ($)': [65, 68, 70, 69, 73.6, 73, 61.5, 62]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

fig.update_layout(title='Government Fiscal Policy Impact on Stock Market Prices',
                  width=800,
                  height=600,
                  xaxis_title='Date',
                  yaxis_title='Price ($)',
                  yaxis_range=[60, 90])

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/92_202312302255.png')