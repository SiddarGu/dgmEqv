
import pandas as pd
import plotly.graph_objects as go

data = [['2019-04-26',50.5,52,54.2,49.8],['2019-04-27',53,52.1,55.2,51.9],['2019-04-28',53,52,53,50.7],['2019-04-29',54,55.7,56.6,53.4],['2019-04-30',55,56.9,57.2,54],['2019-05-01',54.7,54.2,56.1,51.1],['2019-05-02',55,53,57.2,50.3],['2019-05-03',55.3,56.5,58.2,52.4]]

df = pd.DataFrame(data, columns = ['Date','Open','Close','High','Low']) 

fig = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['Open'], close=df['Close'], high=df['High'], low=df['Low'])])

fig.update_layout(title='Trend Analysis of Retail and E-commerce Stock Performance', xaxis_title="Date", yaxis_title="Price ($)",width=800, height=500,yaxis_range=[50, 58])
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/1_202312252244.png')