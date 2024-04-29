
import plotly.graph_objects as go
import pandas as pd

data = [['2020-05-11', 25.7, 29.3, 30.2, 24.3],
        ['2020-05-18', 26.2, 30.7, 31.5, 25.4],
        ['2020-05-25', 27, 31.1, 32.1, 26.3,],
        ['2020-06-01', 27.5, 32.7, 33.6, 27.1],
        ['2020-06-08', 28.5, 33.6, 34.7, 27.4],
        ['2020-06-15', 29.2, 34.2, 35.1, 28.1],
        ['2020-06-22', 30.0, 35.3, 36.2, 29.1],
        ['2020-06-29', 30.5, 36.1, 37.2, 29.8]] 
df = pd.DataFrame(data, columns = ['Period','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Period'], open=df['Opening Price ($)'], high=df['High Price ($)'],
                     low=df['Low Price ($)'], close=df['Closing Price ($)'])])

fig.update_layout(title_text='Financial Trend of Government and Public Policy Sector', 
                  font_size=10,
                  width=800,
                  height=600,
                  yaxis_title='Price ($)')

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/16_202312251608.png')