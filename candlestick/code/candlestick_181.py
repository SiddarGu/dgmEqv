import pandas as pd
import plotly.graph_objects as go

data = {"Date": ["2020-01-01", "2020-02-01", "2020-03-01", "2020-04-01", "2020-05-01", "2020-06-01",
                 "2020-07-01", "2020-08-01", "2020-09-01", "2020-10-01", "2020-11-01", "2020-12-01"],
        "Open Price ($/sq ft)": [450, 470, 492, 500, 520, 530, 550, 570, 590, 610, 630, 650],
        "Close Price ($/sq ft)": [475, 492, 500, 520, 530, 550, 570, 590, 610, 630, 650, 675],
        "High Price ($/sq ft)": [480, 497, 510, 530, 540, 560, 580, 600, 620, 645, 660, 680],
        "Low Price ($/sq ft)": [420, 460, 480, 490, 510, 520, 540, 560, 580, 600, 620, 640]}

df = pd.DataFrame(data)
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($/sq ft)'],
                                     high=df['High Price ($/sq ft)'],
                                     low=df['Low Price ($/sq ft)'],
                                     close=df['Close Price ($/sq ft)'])])

fig.update_layout(title='Monthly Property Price Fluctuation in the Real Estate & Housing Market of 2020',
                  width=1200,
                  height=800,
                  xaxis_rangeslider_visible=False,
                  yaxis_range=[400, 700],
                  autosize=True,
                  showlegend=False,
                  font_family="Arial",
                  font_color="black")

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/130_202312302255.png')