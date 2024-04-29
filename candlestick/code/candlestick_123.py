import pandas as pd
import plotly.graph_objects as go

# Data
data_str = '''Date,Open ($),Close ($),High ($),Low ($)
2020-09-01,270.2,279,285,265
2020-09-08,290,293,295.5,285.5
2020-09-15,302.5,305,307.6,299
2020-09-22,320.5,325,327,312.5
2020-09-29,332.5,337,342,330.5
2020-10-06,349,355,358,345
2020-10-13,352,363,365.5,352
2020-10-20,364.5,378,380.5,356.5
2020-10-27,382,393.5,395.5,372'''

data_list = data_str.split("\n")[1:]
data_list = [row.split(",") for row in data_list]
df = pd.DataFrame(data_list, columns=["Date", "Open", "Close", "High", "Low"])
df[["Open", "Close", "High", "Low"]] = df[["Open", "Close", "High", "Low"]].astype(float)

# Candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open'],
                                     close=df['Close'],
                                     high=df['High'],
                                     low=df['Low'])])

# Layout
fig.update_layout(title='Social Media Company Stock Trends Over Time',
                  width=800,
                  height=600,
                  xaxis_range=[df['Date'].min(), df['Date'].max()],
                  yaxis_range=[df[['Open', 'Close', 'High', 'Low']].min().min() - 10,
                               df[['Open', 'Close', 'High', 'Low']].max().max() + 10])

# Save image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/103_202312302255.png')