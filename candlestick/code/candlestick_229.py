import plotly.graph_objects as go
import pandas as pd

data = {'Date': ['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04', '2019-01-05', '2019-01-06', '2019-01-07', '2019-01-08', '2019-01-09', '2019-01-10'],
        'Open Price ($)': [105, 108, 113, 116, 119, 122, 126, 130, 134, 138],
        'Close Price ($)': [107, 111, 114, 118, 120, 124, 128, 132, 136, 141],
        'High Price ($)': [110, 115, 117, 120, 124, 127, 131, 135, 140, 144],
        'Low Price ($)': [103, 105, 110, 114, 117, 120, 123, 126, 130, 135]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Close Price ($)'])])

fig.update_layout(title='The Financial Performance in a Social Sciences Institutio',
                  width=800,
                  height=600,
                  yaxis_range=[min(df['Low Price ($)'])-5, max(df['High Price ($)'])+5],
                  margin=dict(l=20, r=20, t=40, b=20))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/166_202312302255.png')