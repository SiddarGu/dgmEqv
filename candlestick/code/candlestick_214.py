
import plotly.graph_objects as go
import pandas as pd

data = [['2020-07',30.1,31.2,32.3,29.2],
        ['2020-08',31.6,31.2,32.5,30.7],
        ['2020-09',31.8,31.6,32.9,30.3],
        ['2020-10',32.2,31.7,33.2,30.6],
        ['2020-11',31.5,32.3,33.5,30.2],
        ['2020-12',32.8,33.2,34.1,31.4],
        ['2021-01',33.5,34.1,35.3,32.1],
        ['2021-02',34.3,34.6,35.7,33.2]]

df = pd.DataFrame(data, columns=['Month','Open','Close','High','Low'])

fig = go.Figure(data=[go.Candlestick(x=df['Month'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.update_layout(title="Long-term Electricity Price Trend in the Environment and Sustainability Sector",
                  width=1800,
                  height=1000,
                  yaxis_range=[29.2, 35.7],
                  font=dict(
                    family="sans serif",
                    size=18,
                    color="black"
                  ))

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/8_202312252244.png")