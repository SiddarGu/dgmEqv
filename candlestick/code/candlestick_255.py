import plotly.graph_objects as go
import pandas as pd

data = {
    'Date': ['2021-01-15', '2021-01-22', '2021-01-29', '2021-02-05',
             '2021-02-12', '2021-02-19', '2021-02-26', '2021-03-05'],
    'Open Price ($)': [75.2, 76.6, 78.0, 77.2, 77.8, 80.5, 81.6, 80.7],
    'Close Price ($)': [76.4, 78.3, 77.3, 78.0, 80.1, 81.2, 80.7, 79.3],
    'High Price ($)': [78.5, 79.6, 79.8, 80.2, 82.3, 83.6, 83.8, 82.2],
    'Low Price ($)': [74.9, 75.8, 76.0, 76.1, 77.5, 79.9, 80.1, 78.9]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

fig.update_layout(title='Weekly Freight Transportation Stock Performance Overview',
                  width=800,
                  height=600,
                  xaxis_range=['2021-01-15', '2021-03-05'],
                  font=dict(family='Arial'),
                  margin=dict(l=50, r=50, t=50, b=50))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/114_202312302255.png')