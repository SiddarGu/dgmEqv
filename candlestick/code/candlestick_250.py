
import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame({'Date': ['2020-08-19', '2020-08-26', '2020-09-02', '2020-09-09', '2020-09-16', '2020-09-23', '2020-09-30'],
                   'Open Price ($)': [100.5, 105, 103, 104, 105, 105, 107],
                   'Close Price ($)': [105, 103.1, 102, 106.7, 107.9, 104.4, 108.6],
                   'High Price ($)': [106.2, 107.2, 103, 107.6, 108.2, 106.3, 109.2],
                   'Low Price ($)': [99.8, 101.9, 100.7, 103.4, 104.5, 102.8, 106.2]})

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                    open=df['Open Price ($)'],
                                    high=df['High Price ($)'],
                                    low=df['Low Price ($)'],
                                    close=df['Close Price ($)'])])

fig.update_layout(title_text='Healthcare and Health Stock Performance - Week Overview',
                  yaxis_range=[99.8, 109.2],
                  width=600,
                  height=400
                  )

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/23_202312270043.png')