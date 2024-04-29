
import plotly.graph_objects as go
import pandas as pd

data = [['2020-10-01', 50.2, 54, 56.8, 48.7],
        ['2020-10-02', 56, 58.2, 59.3, 52.1],
        ['2020-10-03', 57.2, 58, 59.5, 54.3],
        ['2020-10-04', 54.5, 56.5, 59.1, 51.3],
        ['2020-10-05', 57.6, 60, 62.5, 55.3],
        ['2020-10-06', 59.4, 62.7, 64.3, 58.2],
        ['2020-10-07', 62.9, 63.2, 65.2, 61.3],
        ['2020-10-08', 60.4, 62.5, 63.8, 58.7]]

df = pd.DataFrame(data, columns=['Date', 'Opening Price ($)', 'Closing Price ($)','High Price ($)','Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
            open=df['Opening Price ($)'],
            high=df['High Price ($)'],
            low=df['Low Price ($)'],
            close=df['Closing Price ($)'])
])

fig.update_layout(title_text='Technology and Internet Companies Stock Prices Over a Week',
                  yaxis_range=[48.7, 65.2],
                  width=800,
                  height=400,
                  font=dict(family="Courier New, monospace",
                  size=12,
                  color="#7f7f7f"))
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/2_202312252244.png')