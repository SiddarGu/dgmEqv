
import plotly.graph_objects as go
import pandas as pd

data = [['2020-05-06',50.5,51.3,52.2,48.7],
        ['2020-05-13',52.2,50.2,54.1,48.9],
        ['2020-05-20',52,53,55,50.5],
        ['2020-05-27',54.2,56.9,59,53.4],
        ['2020-06-03',57,58.2,58.7,54.8],
        ['2020-06-10',59,56.5,60.1,54.2]]

df = pd.DataFrame(data,columns=['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['Opening Price ($)'],
                    high=df['High Price ($)'],
                    low=df['Low Price ($)'],
                    close=df['Closing Price ($)'])])

fig.update_layout(title='Public Policy Investment Performance - 10-Week Overview',
                  xaxis_title='Date',
                  yaxis_title='Price ($)',
                  yaxis_range=[48.7,60.1],
                  font=dict(
                    family="Courier New, monospace",
                    size=14,
                    color="#7f7f7f"
                  ),
                  width=1400,
                  height=800
                  )

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/42_202312252244.png")