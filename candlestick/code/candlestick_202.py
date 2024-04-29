import plotly.graph_objects as go
import pandas as pd

# Data
data = {'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04',
                 '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08'],
        'Open': [125, 127.50, 130, 135, 138, 140, 145, 147],
        'Close': [127.50, 130, 135, 138, 140, 145, 147, 153],
        'High': [128, 132, 136, 140, 143, 147, 151, 154],
        'Low': [123, 126, 129, 133, 137, 138, 141, 142]}

df = pd.DataFrame(data)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create figure
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open'],
                                     high=df['High'],
                                     low=df['Low'],
                                     close=df['Close'])])

# Update layout
fig.update_layout(title='Social Media Company\'s Stock Performance in the First Week of 2022',
                  xaxis_title='Date',
                  yaxis_title='Stock Price',
                  width=800,
                  height=600,
                  yaxis_range=[120, 160],
                  showlegend=False)

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/227_202312302255.png')