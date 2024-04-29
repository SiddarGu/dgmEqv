import plotly.graph_objects as go
import pandas as pd

data = {'Date': ['2022-09-01', '2022-09-02', '2022-09-03', '2022-09-04', '2022-09-05', '2022-09-06', '2022-09-07', '2022-09-08', '2022-09-09', '2022-09-10', '2022-09-11', '2022-09-12', '2022-09-13', '2022-09-14', '2022-09-15', '2022-09-16'],
        'Open Price ($)': [25.00, 27.50, 26.00, 29.00, 30.50, 35.00, 33.00, 36.00, 40.00, 39.00, 42.00, 45.00, 44.00, 47.00, 50.00, 54.00],
        'Close Price ($)': [27.50, 26.00, 29.00, 30.50, 35.00, 33.00, 36.00, 40.00, 39.00, 42.00, 45.00, 44.00, 47.00, 50.00, 54.00, 53.00],
        'High Price ($)': [28.00, 28.50, 30.00, 31.00, 36.00, 35.50, 37.00, 41.00, 42.00, 43.00, 46.00, 46.50, 48.00, 51.00, 55.00, 55.00],
        'Low Price ($)': [24.50, 25.00, 25.50, 28.50, 30.00, 32.00, 32.50, 35.50, 38.00, 38.50, 41.50, 43.00, 43.50, 46.50, 49.50, 52.00]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

fig.update_layout(
    title="September Stock Movement In Agriculture And Food Productio",
    width=1000,
    height=600,
    xaxis=dict(
        rangeslider=dict(
            visible=False
        ),
        title_text="Date"
    ),
    yaxis=dict(
        title_text="Price ($)",
        range=[min(df['Low Price ($)']) - 2, max(df['High Price ($)']) + 2]
    ),
)

fig.update_yaxes(automargin=True)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/99_202312302255.png')
