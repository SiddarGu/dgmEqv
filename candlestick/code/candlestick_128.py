import plotly.graph_objects as go
import pandas as pd
  
data = [('2022-01-01', 15, 17, 18, 13),
        ('2022-01-08', 17, 18, 19, 15),
        ('2022-01-15', 18, 20, 21, 17),
        ('2022-01-22', 20, 19, 21, 18),
        ('2022-01-29', 19, 21, 23, 18),
        ('2022-02-05', 21, 23, 24, 20),
        ('2022-02-12', 23, 25, 26, 22),
        ('2022-02-19', 25, 24, 26, 23),
        ('2022-02-26', 24, 26, 28, 23)]
  
df = pd.DataFrame(data, columns=['Date', 'Open Price ($)', 'Close Price ($)', 'High Price ($)', 'Low Price ($)'])
  
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Close Price ($)'])])

fig.update_layout(title='Monthly Stock Trend of a Sports and Entertainment Company',
                  width=1200, height=800,
                  xaxis_rangeslider_visible=False)
  
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/95_202312302255.png')