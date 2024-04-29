import plotly.graph_objects as go
import pandas as pd

data = [['2018-09-01', 70, 72, 75, 65],
       ['2018-10-01', 72, 71, 75, 70],
       ['2018-11-01', 71, 70, 75, 65],
       ['2018-12-01', 70, 72, 75, 65],
       ['2019-01-01', 71, 70, 76, 66],
       ['2019-02-01', 70, 72, 76, 66],
       ['2019-03-01', 72, 75, 78, 70],
       ['2019-04-01', 75, 76, 80, 70],
       ['2019-05-01', 76, 78, 82, 74],
       ['2019-06-01', 78, 77, 82, 74],
       ['2019-07-01', 77, 76, 80, 70],
       ['2019-08-01', 76, 78, 82, 72],
       ['2019-09-01', 78, 79, 83, 74],
       ['2019-10-01', 79, 80, 84, 74],
       ['2019-11-01', 80, 81, 85, 75],
       ['2019-12-01', 81, 82, 86, 76],
       ['2020-01-01', 82, 83, 87, 78]]

df = pd.DataFrame(data, columns=['Date', 'Opening Price ($)', 'Closing Price ($)', 'High Price ($)', 'Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])

fig.update_layout(title='Monthly Education Stocks Trend (2018 - 2020)', width=800, height=600)
fig.update_yaxes(range=[min(df['Low Price ($)'])-5, max(df['High Price ($)'])+5])

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/173_202312302255.png')