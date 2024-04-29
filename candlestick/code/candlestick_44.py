
import plotly.graph_objects as go
import datetime

#data
dates = ['2019-07-01', '2019-07-08', '2019-07-15', '2019-07-22', '2019-07-29', '2019-08-05', '2019-08-12', '2019-08-19']
opens = [18.4, 19.2, 20.2, 22.4, 25.1, 25.7, 30.1, 25.4]
closes = [17.9, 17.5, 21.3, 25.2, 27.3, 28.9, 28.4, 27.2]
highs = [20.3, 20.4, 22.9, 26.4, 28.6, 30.5, 31.5, 29.6]
lows = [15.7, 16.1, 19.3, 21.2, 24.5, 25.2, 27.2, 22.3]

#init figure
fig = go.Figure(data=[go.Candlestick(x=dates,
                open=opens,
                high=highs,
                low=lows,
                close=closes)])

#update layout
fig.update_layout(title_text='Financial Trend of Charity and Nonprofit Organizations - Weekly Overview',
                  xaxis_rangeslider_visible=False,
                  width=800,
                  height=500,
                  yaxis_range=[min(lows)-1,max(highs)+1])

#write image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/17_202312252244.png')