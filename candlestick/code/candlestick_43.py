
import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame({'Month': ['2019-10', '2019-11', '2019-12', '2020-01', '2020-02', '2020-03', '2020-04'],
                   'Open Price ($)': [50.5, 53, 53, 54, 55, 56, 58],
                   'Close Price ($)': [52, 52.1, 52, 55.7, 56.9, 57, 60],
                   'High Price ($)': [54.2, 55.2, 53, 56.6, 57.2, 60, 62],
                   'Low Price ($)': [49.8, 51.9, 50.7, 53.4, 54, 50, 55]
                   })

fig = go.Figure(data=[go.Candlestick(
    x=df['Month'],
    open=df['Open Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)'],
    close=df['Close Price ($)']
)])

fig.update_layout(
    title_text="Financial Trend of Science and Engineering Companies - Monthly Overview",
    xaxis_rangeslider_visible=False,
    yaxis_range=[min(df['Low Price ($)'])-1, max(df['High Price ($)'])+1],
    width=800,
    height=500,
    font_size=10,
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/13_202312270043.png')