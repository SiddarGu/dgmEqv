
import plotly.graph_objects as go
import pandas as pd

data = [['2019-03-02',310,320,322,305],
        ['2019-03-09',320,325,330,315],
        ['2019-03-16',320,335,338,316],
        ['2019-03-23',340,335,342,330],
        ['2019-03-30',335,340,345,335],
        ['2019-04-06',350,348,352,345],
        ['2019-04-13',345,347,350,340],
        ['2019-04-20',355,345,357,342]]

df = pd.DataFrame(data,columns=['Date','Opening Price ($)','Closing Price ($)','High Price ($)','Low Price ($)'])

fig = go.Figure(data=[go.Candlestick(x=df['Date'],open=df['Opening Price ($)'],high=df['High Price ($)'],low=df['Low Price ($)'],close=df['Closing Price ($)'])])

fig.update_layout(title_text="Financial Trends of Tourism and Hospitality Sector",width=800, height=400, yaxis_range=[min(df['Low Price ($)'])-2,max(df['High Price ($)'])+2])

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/24_202312270043.png')