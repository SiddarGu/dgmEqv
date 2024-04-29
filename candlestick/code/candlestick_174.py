import plotly.graph_objects as go
import pandas as pd
 
data = {'Date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08'],
        'Open Price ($)': [120, 122.5, 124, 123, 126, 129, 133, 131],
        'Close Price ($)': [122, 123.75, 122.5, 125.5, 128, 132, 130, 134],
        'High Price ($)': [125, 126, 128, 128.5, 130, 135, 134, 137],
        'Low Price ($)': [117, 120, 121, 122, 125, 127, 128, 129]}
 
df = pd.DataFrame(data)
 
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Close Price ($)'])])
 
fig.update_layout(title='Stock Price Trends of Sports and Entertainment Companies',
                  width=800,
                  height=600,
                  showlegend=False,
                  yaxis_range=[min(df['Low Price ($)']) - 2, max(df['High Price ($)']) + 2],
                  xaxis=dict(
                    tickmode='auto',
                    nticks=10),
                  yaxis=dict(
                    title='Price ($)'),
                  xaxis_rangeslider_visible=False)
 
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/214_202312302255.png')