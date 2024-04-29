
import plotly.graph_objects as go
import pandas as pd

data = [['2019-04-26',50.5,52.8,54.2,49.8],
        ['2019-04-27',53.2,52.1,55.2,51.9],
        ['2019-04-28',53.1,52.9,54.2,50.7],
        ['2019-04-29',54.2,55.7,56.6,53.4],
        ['2019-04-30',55.3,56.9,57.2,54.1],
        ['2019-05-01',54.5,56.2,57.0,52.6],
        ['2019-05-02',54.1,53.5,55.2,51.2],
        ['2019-05-03',50.9,51.3,52.3,49.9],
        ['2019-05-04',50.3,51.4,52.3,49.2]]

df = pd.DataFrame(data, columns=['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])
fig.update_layout(title='Financial Trend of Law and Legal Affairs - Weekly Overview',
              yaxis_range=[min(df['Low Price ($)'])-1,max(df['High Price ($)'])+1],
              width=1000, height=800)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/46_202312252244.png')