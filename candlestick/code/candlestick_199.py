import plotly.graph_objects as go
import pandas as pd

data = {
    'Date': ['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04', '2019-01-05', '2019-01-06', '2019-01-07', '2019-01-08', '2019-01-09', '2019-01-10', '2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14', '2019-01-15'],
    'Opening Price ($)': [200, 212, 216, 222, 230, 235, 238, 242, 248, 255, 258, 263, 267, 270, 277],
    'Closing Price ($)': [210.2, 215, 220, 228, 232, 236, 240, 248, 253, 257, 262, 265, 269, 275, 280],
    'High Price ($)': [213.4, 217.6, 222.8, 232.1, 236.4, 237.6, 243, 250.4, 257.2, 259.6, 265.8, 267.8, 273, 279.2, 284.4],
    'Low Price ($)': [190, 200, 202, 215, 220.8, 223, 228, 234, 240, 242, 248, 253, 258, 263, 268]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])

fig.update_layout(title='Monthly Government Bond Yield Trend',
                  width=900,
                  height=600,
                  xaxis_rangeslider_visible=False,
                  xaxis=dict(tickfont=dict(size=8)),
                  yaxis=dict(tickfont=dict(size=8)))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/126_202312302255.png')