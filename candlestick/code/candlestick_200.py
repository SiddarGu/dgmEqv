
import plotly.graph_objects as go
import pandas as pd

data = [['2019-06',4500,4600,4700,4400],['2019-07',4600,4700,4800,4500],['2019-08',4700,4800,4900,4600],['2019-09',4800,4900,5000,4700],['2019-10',4800,5000,5100,4800],['2019-11',5000,5100,5200,4900],['2019-12',5100,5200,5300,5000]]
df = pd.DataFrame(data,columns=['Month','Open Price ($)','Close Price ($)','High Price ($)','Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Month'],
                open=df['Open Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Close Price ($)'])])

fig.update_layout(title = 'Real Estate and Housing Market Trend Analysis',yaxis_range = [4300,5300], width=800, height=400,font=dict(family="monospace"))
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/44_202312252244.png')