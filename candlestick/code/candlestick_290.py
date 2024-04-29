
import plotly.graph_objects as go
import pandas as pd

data = [['2019-05-01', 50.5, 53.2, 54.5, 49.2],
        ['2019-05-02', 52.0, 51.9, 54.5, 49.5],
        ['2019-05-03', 52.0, 53.2, 54.9, 51.2],
        ['2019-05-04', 54.0, 53.1, 55.2, 51.2],
        ['2019-05-05', 53.5, 54.2, 55.9, 51.5],
        ['2019-05-06', 55.6, 58.0, 59.0, 55.3],
        ['2019-05-07', 58.2, 57.1, 59.5, 54.2]]

df = pd.DataFrame(data, columns = ['Date','Opening Price ($)', 'Closing Price ($)', 'High Price ($)', 'Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])

fig.update_layout(title="Science and Engineering Stock Price Trend Analysis",
                  xaxis_title="Date",
                  yaxis_title="Price ($)",
                  yaxis_range=[min(df['Low Price ($)'])-2, max(df['High Price ($)'])+2],
                  width=800,
                  height=400)

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/20_202312270043.png")