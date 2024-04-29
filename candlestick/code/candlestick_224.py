import pandas as pd
import plotly.graph_objects as go

# Define the data
data = {
    'Date': ['2019-04-01', '2019-04-02', '2019-04-03', '2019-04-04', '2019-04-05'],
    'Open Price ($)': [38, 40, 42, 46, 48],
    'Close Price ($)': [39.6, 42.1, 45, 45.8, 47.9],
    'High Price ($)': [40, 42.5, 47, 48.5, 48.9],
    'Low Price ($)': [36.5, 39.6, 41, 44, 46.5]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert the date column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

# Update the figure layout
fig.update_layout(title="Law Firm Stock Price Fluctuation - April 2019",
                  width=800,
                  height=600,
                  xaxis_rangeslider_visible=False)

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/164_202312302255.png')