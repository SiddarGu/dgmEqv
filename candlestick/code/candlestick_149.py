import plotly.graph_objects as go
import pandas as pd

data = [['2020-02-01', 20.5, 22.3, 24.5, 19.1],
        ['2020-02-08', 22.3, 23.6, 24.9, 20.5],
        ['2020-02-15', 23.6, 24.2, 25.6, 21.8],
        ['2020-02-22', 24.2, 23.7, 25.4, 21.9],
        ['2020-02-29', 23.7, 21.9, 24.8, 20.5],
        ['2020-03-07', 21.9, 19.5, 23.9, 18.3],
        ['2020-03-14', 19.5, 18.3, 21.8, 16.1],
        ['2020-03-21', 18.3, 17.2, 20.5, 15.0],
        ['2020-03-28', 17.2, 16.5, 19.4, 14.3]]

df = pd.DataFrame(data, columns=['Date', 'Opening Price ($)', 'Closing Price ($)', 'High Price ($)', 'Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Opening Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Closing Price ($)'])])

fig.update_layout(
    title='Food and Beverage Industry Stock Prices for Q1 2020',
    xaxis_title='Date',
    yaxis_title='Price ($)',
    width=1000,
    height=600,
    margin=dict(l=50, r=50, t=80, b=50),
    yaxis_range=[min(df['Low Price ($)']) - 1, max(df['High Price ($)']) + 1]
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/202_202312302255.png')