import plotly.graph_objects as go
import pandas as pd

# Define the data
data = {'Date': ['2020-08-03', '2020-08-10', '2020-08-17', '2020-08-24', '2020-08-31', '2020-09-07', '2020-09-14', '2020-09-21'],
        'Open Price ($)': [138.5, 140.1, 141.2, 140.5, 139.5, 138.9, 137.8, 136.1],
        'Close Price ($)': [139.7, 141.5, 142.8, 141.7, 140.7, 140.3, 139.2, 137.5],
        'High Price ($)': [140.2, 142.5, 144.2, 143.1, 142.0, 141.7, 140.6, 138.9],
        'Low Price ($)': [135.4, 136.2, 137.5, 137.8, 136.3, 135.5, 134.7, 133.6]}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert the Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Close Price ($)'])])

# Update the layout
fig.update_layout(title="Stock Trends in Science and Engineering Sector",
                  width=800,
                  height=600,
                  xaxis_rangeslider_visible=False,
                  showlegend=False,
                  yaxis_range=[min(df['Low Price ($)'])-1, max(df['High Price ($)'])+1])

# Save the figure
fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/182_202312302255.png")