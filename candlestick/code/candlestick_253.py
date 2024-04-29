import plotly.graph_objects as go
import pandas as pd

# Create DataFrame
data = {'Date': ['2019-11-01', '2019-11-02', '2019-11-03', '2019-11-04', '2019-11-05', '2019-11-06', '2019-11-07', '2019-11-08', '2019-11-09', '2019-11-10'],
        'Opening Price ($)': [2500, 2545, 2535, 2540, 2545, 2555, 2560, 2575, 2575, 2580],
        'Closing Price ($)': [2540, 2530, 2545, 2545, 2550, 2550, 2570, 2570, 2580, 2585],
        'High Price ($)': [2560, 2555, 2565, 2560, 2570, 2580, 2590, 2590, 2590, 2600],
        'Low Price ($)': [2480, 2510, 2520, 2530, 2540, 2550, 2555, 2560, 2565, 2570]}

df = pd.DataFrame(data)

# Convert date column to a datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Opening Price ($)'],
                                     close=df['Closing Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'])])

# Update layout
fig.update_layout(title='Government Bond Price Trend in November 2019',
                  xaxis_title='Date',
                  yaxis_title='Price ($)',
                  width=1200,
                  height=800,
                  margin=dict(l=40, r=40, b=40, t=40),
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  showlegend=False,
                  font=dict(family='sans-serif', size=10),
                  yaxis=dict(range=[min(df['Low Price ($)'])-50, max(df['High Price ($)'])+50]))

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/153_202312302255.png')