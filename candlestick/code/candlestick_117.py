import plotly.graph_objects as go
import pandas as pd

data = {'Date': ['2021-11-01', '2021-11-02', '2021-11-03', '2021-11-04', '2021-11-05', '2021-11-06', '2021-11-07', '2021-11-08', '2021-11-09', '2021-11-10', '2021-11-11', '2021-11-12', '2021-11-13', '2021-11-14', '2021-11-15'],
        'Open': [80, 85, 87, 90, 93, 105, 110, 105, 110, 114, 122, 117, 120, 122, 130],
        'Close': [90, 86, 88, 95, 102, 107, 106, 110, 115, 120, 117, 118, 119, 125, 128],
        'High': [100, 94, 95, 105, 108, 115, 115, 120, 126, 130, 132, 130, 135, 140, 142],
        'Low': [70, 80, 82, 85, 89, 90, 100, 100, 100, 110, 108, 115, 115, 120, 122]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open'],
                                     close=df['Close'],
                                     high=df['High'],
                                     low=df['Low'])])

fig.update_layout(title='November 2021 Retail and E-commerce Stock Market Analysis',
                  xaxis=dict(title='Date'),
                  yaxis=dict(title='Price'),
                  width=800,
                  height=600)

fig.update_yaxes(autorange=True)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/132_202312302255.png')