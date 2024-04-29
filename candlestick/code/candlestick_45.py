
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

#data
data = {'Date':['2019-06-09','2019-06-10','2019-06-11','2019-06-12','2019-06-13','2019-06-14','2019-06-15','2019-06-16'],
'Opening Price ($)':[80.1,81.4,81.6,84.5,84.3,85.7,86.3,86.5],
'Closing Price ($)':[81.3,81.5,83.5,84.2,85.4,86.3,86.7,88.2],
'High Price ($)':[81.8,83.1,83.6,85.4,85.7,87.4,87.6,88.6],
'Low Price ($)':[79.7,80.3,80.9,83.2,83.9,85.2,84.9,85.9]}

df = pd.DataFrame(data)

#plot
fig = go.Figure(data = [go.Candlestick(x=df['Date'], open=df['Opening Price ($)'], high=df['High Price ($)'],
low=df['Low Price ($)'], close=df['Closing Price ($)'])])

#update layout
fig.update_layout(width=1000, height=500, title_text="Government and Public Policy Financial Trend Analysis", yaxis_range=[79,89])

#save
pio.write_image(fig, '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/16_202312252244.png')