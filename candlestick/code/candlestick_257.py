
import plotly.graph_objects as go
import pandas as pd

data = [['2019-04-26',50.5,52,54.2,49.8],
        ['2019-04-27',53,52.1,55.2,51.9],
        ['2019-04-28',53,52,53,50.7],
        ['2019-04-29',54,55.7,56.6,53.4],
        ['2019-04-30',55,56.9,57.2,54],
        ['2019-05-01',54.3,55.8,56.5,53.2],
        ['2019-05-02',55.1,56.6,57.3,54.4],
        ['2019-05-03',55.5,57,57.5,54.5],
        ['2019-05-04',56.6,57.4,58,55.9],
        ['2019-05-05',57,58.2,58.5,55.2]]

df = pd.DataFrame(data, columns = ['Date','Opening Price ($)','Closing Price ($)','High Price ($)', 'Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])

fig.update_layout(title_text='Financial Trend of Retail and E-commerce Companies - Weekly Overview',
                  width=800,
                  height=400,
                  yaxis_range=[48,60])

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/10_202312251608.png')