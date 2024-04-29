
import plotly.graph_objects as go
import pandas as pd

data = [['2019-05-01', 25.3, 29.8, 30.2, 24.9], 
        ['2019-05-02', 29.6, 29.2, 31.5, 27.8], 
        ['2019-05-03', 29.7, 30.2, 31.2, 28.3], 
        ['2019-05-04', 31.1, 31.2, 32.5, 30.3], 
        ['2019-05-05', 31.8, 31.6, 33.2, 30.8], 
        ['2019-05-06', 32.4, 30.2, 33.1, 29.7], 
        ['2019-05-07', 30.2, 31.1, 31.8, 29.4]]
df = pd.DataFrame(data,columns=['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])
fig.update_layout(title={'text':'Technology and Internet Company Stock Performance - Weekly Overview', 
                         'y':0.9, 
                         'x':0.5, 
                         'xanchor': 'center', 
                         'yanchor': 'top'},
                  yaxis_range=[24.9,33.2], 
                  width=800, 
                  height=400, 
                  font=dict(size=14))

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/4_202312270043.png")