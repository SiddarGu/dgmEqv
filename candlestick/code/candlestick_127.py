import pandas as pd
import plotly.graph_objects as go

# Define the data
data = {
    'Date': ['2020-11-01', '2020-11-08', '2020-11-15', '2020-11-22', '2020-11-29', '2020-12-06', '2020-12-13', '2020-12-20', '2020-12-27', '2021-01-03', '2021-01-10', '2021-01-17', '2021-01-24', '2021-01-31', '2021-02-07', '2021-02-14'],
    'Open Price ($)': [20, 22, 21, 23, 24, 27, 30, 35, 40, 48, 47, 48, 50, 52, 48, 45],
    'Close Price ($)': [22, 20, 22, 24, 27, 30, 35, 40, 48, 47, 48, 50, 52, 48, 45, 50],
    'High Price ($)': [23, 24, 23, 25, 28, 32, 38, 42, 52, 50, 50, 54, 55, 59, 54, 56],
    'Low Price ($)': [18, 19, 19, 20, 22, 24, 27, 30, 35, 40, 43, 46, 46, 46, 38, 40]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

# Set the title and size parameters
fig.update_layout(
    title='Weekly Logistics Company Stocks Trend',
    width=1200,
    height=800,
    margin=dict(l=50, r=50, t=80, b=50),
    yaxis_range=[min(df['Low Price ($)']) * 0.95, max(df['High Price ($)']) * 1.05]
)

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/54_202312302255.png')