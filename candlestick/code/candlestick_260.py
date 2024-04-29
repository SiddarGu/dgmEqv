
import plotly.graph_objects as go
import pandas as pd

data = {'Date':['2020-10-03','2020-10-10','2020-10-17','2020-10-24','2020-10-31','2020-11-07','2020-11-14'],
        'Opening Price ($)':[31.2,32.4,31.3,32.7,31.2,31.4,31.2],
        'Closing Price ($)':[31.9,31.7,32.2,31.3,30.9,31.7,30.8],
        'High Price ($)':[32.3,33.2,33.2,32.9,31.4,32.4,31.4],
        'Low Price ($)':[30.9,30.6,30.5,30.1,30.7,30.9,30.4]}
df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])
fig.update_layout(title='Energy and Utilities Stock Trend Analysis over One Month',
                  xaxis_title='Date',
                  yaxis_title='Price ($)',
                  yaxis_range=[30, 33.5],
                  width=1000,
                  height=500,
                  font_size=12,
                  font_family='sans-serif')
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/34_202312252244.png')