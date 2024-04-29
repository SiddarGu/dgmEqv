
import plotly.graph_objects as go
import pandas as pd

data = {'Date': ['2019-05-01','2019-05-08','2019-05-15','2019-05-22','2019-05-29','2019-06-05','2019-06-12','2019-06-19'],
       'Opening Price ($)' : [350,375,410,390,420,415,385,405],
       'Closing Price ($)' : [370,400,405,420,430,400,405,410],
       'High Price ($)' : [395,410,420,440,455,430,420,420],
       'Low Price ($)' : [325,360,380,375,400,385,370,395]
      }

df = pd.DataFrame.from_dict(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])

fig.update_layout(title_text="Real Estate and Housing Market Prices - Weekly Overview",
                  yaxis_range=[df['Low Price ($)'].min(), df['High Price ($)'].max()],
                  width=800,
                  height=800,
                  font=dict(family="sans serif"))

fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/17_202312270043.png")