import plotly.graph_objects as go
import pandas as pd


data = {
    'Date': ['2021-01-04', '2021-01-11', '2021-01-18', '2021-01-25', '2021-02-01', '2021-02-08', '2021-02-15'],
    'Open Price ($)': [35.4, 37, 38.2, 40.5, 42, 45.3, 49.4],
    'Close Price ($)': [37.2, 39, 40.1, 41.6, 43.5, 44.8, 50.7],
    'High Price ($)': [38, 40.3, 42.5, 42.6, 44.5, 47.8, 51.4],
    'Low Price ($)': [34.8, 36.5, 37.8, 38.2, 41.9, 43, 48.1]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Close Price ($)'])])

fig.update_layout(title='Weekly Trends of Fine Art Auction Prices',
                  width=800,
                  height=600,
                  xaxis_range=['2021-01-01', '2021-02-20'],
                  yaxis_range=[30, 55],
                  template='plotly_white')

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/158_202312302255.png')