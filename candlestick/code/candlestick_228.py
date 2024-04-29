import plotly.graph_objects as go
import pandas as pd

data = {
    'Date': ['2019-01-07', '2019-01-14', '2019-01-21', '2019-01-28', '2019-02-04', '2019-02-11', '2019-02-18', '2019-02-25'],
    'Opening Price ($)': [75.8, 82, 84, 86.5, 85.8, 78, 79.9, 81],
    'Closing Price ($)': [80.1, 83.3, 85.1, 85.7, 87.2, 80.1, 80.5, 80.6],
    'High Price ($)': [80.6, 84.6, 88.9, 88, 88, 81, 82.1, 82.3],
    'Low Price ($)': [74.5, 81.8, 83.7, 84, 85, 75.1, 79.2, 79.1]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])

fig.update_layout(
    title='Weekly Stock Price Movement in Law Firms',
    width=800,
    height=600,
    yaxis_range=[70, 95]
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/151_202312302255.png')