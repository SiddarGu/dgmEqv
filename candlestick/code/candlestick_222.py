
import plotly.graph_objects as go
import pandas as pd

df = pd.DataFrame({'Date':['2018-10-23','2018-11-01','2018-11-08','2018-11-15','2018-11-22','2018-11-29','2018-12-06'], 
                   'Opening Price ($)':[54,48,55,50.5,51,53,56], 
                   'Closing Price ($)':[51,50,52,56,55.5,50,52.3], 
                   'High Price ($)':[62.3,58.4,60,59.1,60.2,57,60.2], 
                   'Low Price ($)':[45,44.2,45.6,49,48,48.5,49.5]})

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])
fig.update_layout(title='Healthcare and Health Industry Stock Trend Analysis',
                  yaxis_range=[40,63],
                  width=800, height=500,
                  font=dict(size=12))
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/27_202312252244.png')