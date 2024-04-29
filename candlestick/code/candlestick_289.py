
import plotly.graph_objects as go
import pandas as pd

data = [['2020-08-04',50.5,53,54.2,49.8],
        ['2020-08-11',52,54.1,55.2,51.9],
        ['2020-08-18',53,52,53,50.7],
        ['2020-08-25',54,55.7,56.6,53.4],
        ['2020-09-01',55,56.9,57.2,54],
        ['2020-09-08',56.1,58.6,59.2,54.9]]

df = pd.DataFrame(data, columns=['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])

fig.update_layout(title='Logistics & Transportation Industry Financial Trend Overview',
                  yaxis_title='Price ($)',
                  font={'family': 'sans-serif'},
                  xaxis_rangeslider_visible=False,
                  xaxis_showgrid=False,
                  yaxis_showgrid=False,
                  width=800,
                  height=800,
                  margin=dict(t=25, b=25, l=25, r=25))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/14_202312251608.png')