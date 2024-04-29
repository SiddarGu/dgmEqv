

import plotly.graph_objects as go
import pandas as pd

data = [['2022-05',90,93,95,87],
        ['2022-06',95,94,97,91],
        ['2022-07',93,96,98,90],
        ['2022-08',92,90,93,88],
        ['2022-09',94,90,95,87],
        ['2022-10',92,90,93,87]]

df = pd.DataFrame(data, columns = ['Month','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Month'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])

fig.update_layout(title_text='Monthly Price Trend of Education and Academics Stock',
                  width=800, height=400,
                  yaxis_range=[85,100])

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/5_202312251608.png')