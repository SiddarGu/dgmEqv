
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

#set up data
data = [['2019-05-02',50,60,70,40],['2019-05-09',70,60,80,50],['2019-05-16',60,70,80,50],['2019-05-23',70,60,80,50],['2019-05-30',60,70,80,50],['2019-06-06',70,60,80,50],['2019-06-13',60,70,80,50],['2019-06-20',70,60,80,50]]
df = pd.DataFrame(data, columns=['Date','Open','Close','High','Low'])

#create figure
fig = go.Figure(data=[go.Candlestick(x=df['Date'], open=df['Open'], high=df['High'], low=df['Low'], close=df['Close'])])

#update figure layout
fig.update_layout(title_text='Financial Trends in Environment and Sustainability Sector', width=800, height=500, yaxis_range=[35,85])

#save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/6_202312252244.png')