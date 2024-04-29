import plotly.graph_objects as go
import pandas as pd

# Data
data = [['2022-01-03', 80.2, 83, 85.6, 79],
        ['2022-01-10', 82.9, 85, 88, 82],
        ['2022-01-17', 85.5, 88.7, 90.2, 85],
        ['2022-01-24', 88.1, 91, 92.2, 87.6],
        ['2022-01-31', 90.1, 93.8, 96, 89.8],
        ['2022-02-07', 93, 96.5, 98.3, 92.4],
        ['2022-02-14', 95.4, 98, 100.6, 94.8],
        ['2022-02-21', 97.2, 100.6, 103.2, 97]]

df = pd.DataFrame(data, columns=['Date', 'Open Price ($)', 'Close Price ($)', 'High Price ($)', 'Low Price ($)'])

# Candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])]
               )

# Figure layout
fig.update_layout(title='Weekly Stock Price Movement in Healthcare Sector',
                  width=800,
                  height=600,
                  xaxis=dict(
                      rangeslider=dict(
                          visible=False
                      ),
                      type='date'
                  ),
                  yaxis=dict(
                      range=[75, 105]
                  )
                  )

# Save image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/212_202312302255.png')