
import plotly.graph_objects as go
import pandas as pd

data = [
    ['2019-04-20',50,52.9,53.5,48.0],
    ['2019-04-21',51.2,51,52.4,49.1],
    ['2019-04-22',51.6,50,52.2,48.5],
    ['2019-04-23',52.5,53.2,54.1,51.3],
    ['2019-04-24',53.1,51.8,54.0,50.2],
    ['2019-04-25',52,50,52.8,49.3],
]

df = pd.DataFrame(data, columns=['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                       open=df['Opening Price ($)'],
                       high=df['High Price ($)'],
                       low=df['Low Price ($)'],
                       close=df['Closing Price ($)'])
            ])

fig.update_layout(title_text='Financial Trend of Charity and Nonprofit Organizations - Week Overview',
                  yaxis_range=[min(df['Low Price ($)']),max(df['High Price ($)'])])
fig.update_layout(width=900, height=800)
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/3_202312252244.png')