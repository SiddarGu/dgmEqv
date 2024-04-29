
import plotly.graph_objects as go
import pandas as pd

data = [['2019-01',3,5.6,6.2,2.2],['2019-02',3,5.9,6.7,2.7],['2019-03',3,6.1,6.3,2.9],['2019-04',3,6.4,7.0,2.5],['2019-05',3,6.8,7.7,2.2],['2019-06',3,7.1,8.4,2.0],['2019-07',3,7.3,8.1,1.8],['2019-08',3,7.5,8.8,1.7]]

df = pd.DataFrame(data, columns = ['Month', 'Average Wage (USD)', 'Employment Rate (%)', 'Unemployment Rate (%)', 'Quit Rate (%)']) 

fig = go.Figure(data=[go.Candlestick(x=df['Month'], 
                open=df['Employment Rate (%)'],
                high=df['Unemployment Rate (%)'],
                low=df['Quit Rate (%)'],
                close=df['Average Wage (USD)'])])

fig.update_layout(title="Human Resources and Employee Management Statistics - Monthly Overview", xaxis_title="Month", yaxis_title="Value",
                  width=1000, height=800, yaxis_range=[0, 9], font=dict(family="Franklin Gothic Book, sans-serif"))
fig.update_layout(autosize=False, width=1000, height=800)

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/1_202312251608.png")