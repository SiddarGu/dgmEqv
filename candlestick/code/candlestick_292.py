
import plotly.graph_objects as go
import pandas as pd

data = [['2019-04-26',50.5,52,54.2,49.8],['2019-04-27',53,52.1,55.2,51.9],['2019-04-28',53,52,53,50.7],['2019-04-29',54,55.7,56.6,53.4],['2019-04-30',55,56.9,57.2,54],['2019-05-01',59.2,58.3,60.2,56.8],['2019-05-02',59.5,58.8,60,57.6],['2019-05-03',60,58.2,60.9,56.2],['2019-05-04',58,58.1,59.5,57.2],['2019-05-05',58.5,57.2,60.3,55.1]]
df=pd.DataFrame(data,columns=['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['Opening Price ($)'], high=df['High Price ($)'],low=df['Low Price ($)'], close=df['Closing Price ($)'])])
fig.update_layout(title_text='Financial Trend in Government and Public Policy - Week Overview', width=1000, height=1000, yaxis_range=[48,61])
fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/18_202312270043.png")