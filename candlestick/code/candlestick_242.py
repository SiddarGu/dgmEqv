
import plotly.graph_objects as go
import pandas as pd

#Read data
data = [['2020-07-20',50.2,51.2,52.3,50],['2020-07-27',50,51.2,52.1,48.5],['2020-08-03',49.5,51.8,52.2,47.9],['2020-08-10',51.2,53.1,53.5,50],['2020-08-17',52.1,54.3,54.7,50.9],['2020-08-24',53,53.7,54.5,52.2],['2020-08-31',52.3,53.4,54.1,51.8]]
df = pd.DataFrame(data, columns=['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])

#Plot candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])

#Set figure size and title
fig.update_layout(title_text='Weekly Stock Price of Law and Legal Affairs Companies', width=800, height=400, yaxis_range=[45,55])

#Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/4_202312251608.png')