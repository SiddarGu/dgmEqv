import plotly.graph_objects as go
import pandas as pd

data = {
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05', '2021-01-06',
             '2021-01-07', '2021-01-08', '2021-01-09', '2021-01-10', '2021-01-11', '2021-01-12',
             '2021-01-13', '2021-01-14', '2021-01-15', '2021-01-16', '2021-01-17', '2021-01-18',
             '2021-01-19', '2021-01-20'],
    'Opening Donations ($)': [5000, 5050, 5150, 5200, 5350, 5400, 5550, 5600, 5750, 5850, 5950,
                              6000, 6100, 6250, 6350, 6450, 6500, 6600, 6700, 6800],
    'Closing Donations ($)': [5050, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000,
                              6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900],
    'High Donations ($)': [5200, 5200, 5400, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100,
                            6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000],
    'Low Donations ($)': [4900, 5000, 5100, 5150, 5200, 5300, 5400, 5500, 5600, 5800, 5900,
                           5950, 6050, 6200, 6300, 6400, 6450, 6550, 6650, 6750]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Opening Donations ($)'],
    close=df['Closing Donations ($)'],
    high=df['High Donations ($)'],
    low=df['Low Donations ($)']
)])

fig.update_layout(title='Charitable Donations Trend for January 2021 in Nonprofit Organizations',
                  width=800, height=600,
                  xaxis_rangeslider_visible=False)
fig.update_yaxes(range=[min(df['Low Donations ($)']) - 100, max(df['High Donations ($)']) + 100])

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/190_202312302255.png', engine="kaleido")
