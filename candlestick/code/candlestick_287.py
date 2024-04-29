import plotly.graph_objects as go
import pandas as pd

data = {
    'Date': ['2022-03-01', '2022-03-02', '2022-03-03', '2022-03-04', '2022-03-05', '2022-03-06', '2022-03-07', '2022-03-08', '2022-03-09', '2022-03-10'],
    'Open Price ($)': [78.5, 80.2, 80.7, 82.5, 83, 84, 84.5, 85, 88, 87.5],
    'Close Price ($)': [80, 81.6, 83, 84, 85, 86.2, 87.3, 88.4, 89, 90.4],
    'High Price ($)': [82.5, 82, 84.3, 84.5, 86, 87, 88.5, 89, 90.5, 92],
    'Low Price ($)': [77.65, 79.6, 80.1, 81.7, 83.3, 83.5, 84, 84.6, 87.5, 86]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Close Price ($)'])])

fig.update_layout(
    title='Energy and Utilities Market Activity - Early March 2022 Trends',
    width=800,
    height=600,
    xaxis=dict(
        rangeslider=dict(
            visible=False
        )
    ),
    yaxis_range=[df['Low Price ($)'].min() - 1, df['High Price ($)'].max() + 1]
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/217_202312302255.png')