import pandas as pd
import plotly.graph_objects as go

# Data
data = {'Date': ['2021-01-10', '2021-01-17', '2021-01-24', '2021-01-31', '2021-02-07', '2021-02-14', '2021-02-21',
                 '2021-02-28', '2021-03-07', '2021-03-14', '2021-03-21', '2021-03-28', '2021-04-04', '2021-04-11',
                 '2021-04-18', '2021-04-25'],
        'Open Price ($)': [101, 107, 106, 102, 118, 120, 124, 125, 134, 136, 141, 146, 150, 152, 155, 160],
        'Close Price ($)': [105, 108, 105, 112, 120, 122, 123, 130, 135, 140, 145, 148, 151, 154, 160, 165],
        'High Price ($)': [108, 112, 110, 120, 125, 130, 132, 135, 140, 142, 147, 150, 153, 157, 162, 167],
        'Low Price ($)': [98, 100, 104, 101, 115, 110, 120, 121, 130, 130, 132, 142, 146, 149, 152, 158]}

df = pd.DataFrame(data)

# Candlestick Chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

# Chart Layout
fig.update_layout(title='Stock Price Movement in the Health and Healthcare Sector over the first quarter of 2021',
                  width=800,
                  height=600,
                  xaxis=dict(title='Date'),
                  yaxis=dict(title='Price ($)',
                             range=[min(df['Low Price ($)']) - 10, max(df['High Price ($)']) + 10]),
                  showlegend=False)

# Save Image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/111_202312302255.png')