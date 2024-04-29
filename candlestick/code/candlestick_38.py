
import plotly.graph_objects as go
import pandas as pd 

data = [['2019-04-26',1000,1050,1090,950],
        ['2019-04-27',1020,1030,1060,990],
        ['2019-04-28',1100,1050,1150,1020],
        ['2019-04-29',1020,1050,1060,980],
        ['2019-04-30',1150,1160,1180,1100],
        ['2019-05-01',1050,1090,1110,1020],
        ['2019-05-02',1020,1050,1080,990]]
df = pd.DataFrame(data, columns = ['Date','Open','Close','High','Low'])
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                       open=df['Open'],
                       high=df['High'],
                       low=df['Low'],
                       close=df['Close'])])

fig.update_layout(title='Financial Trend of Education and Academics Sector',
                  xaxis_range=['2019-04-26','2019-05-02'],
                  yaxis_range=[950,1180],
                  width=850,
                  height=850)

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/4_202312252244.png")