import plotly.graph_objects as go
import pandas as pd

# Define data
data = {'Date': ['2021-01-04', '2021-01-11', '2021-01-18', '2021-01-25', '2021-02-01', '2021-02-08'],
        'Opening Price ($)': [135.3, 133.8, 142.3, 142.0, 151.2, 154.8],
        'Closing Price ($)': [133.6, 142.1, 141.1, 150.9, 152.6, 161.1],
        'High Price ($)': [139.7, 144.3, 147.6, 153.2, 157.3, 164.2],
        'Low Price ($)': [129.1, 130.4, 139.8, 138.7, 147.9, 152.4]
        }

df = pd.DataFrame(data)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Opening Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Closing Price ($)'])])

# Set layout
fig.update_layout(title='Social Media Market Overview - 2021 Q1 Performance',
                  autosize=False,
                  width=800,
                  height=600,
                  margin=dict(l=50, r=50, t=50, b=50),
                  yaxis_range=[120, 170])

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/90_202312302255.png')