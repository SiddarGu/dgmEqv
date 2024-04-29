import plotly.graph_objects as go
import pandas as pd

# Data
data = {
    "Date": [
        "2020-01-01", "2020-01-08", "2020-01-15", "2020-01-22", "2020-01-29", 
        "2020-02-05", "2020-02-12", "2020-02-19", "2020-02-26"
    ],
    "Opening Value in $ (Million)": [
        107.2, 112.3, 115.7, 114.5, 117.8, 116.8, 118.2, 120.3, 122.7
    ],
    "Closing Value in $ (Million)": [
        112.3, 115.7, 114.5, 117.8, 116.8, 118.2, 120.3, 122.7, 121.4
    ],
    "Highest Value in $ (Million)": [
        116.8, 118.4, 119.7, 121.5, 122.4, 122.9, 125.6, 126.9, 127.2
    ],
    "Lowest Value in $ (Million)": [
        104.6, 109.2, 112.0, 112.4, 114.7, 115.1, 116.5, 118.9, 119.9
    ],
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Opening Value in $ (Million)'],
    high=df['Highest Value in $ (Million)'],
    low=df['Lowest Value in $ (Million)'],
    close=df['Closing Value in $ (Million)']
)])

# Update layout
fig.update_layout(
    title="Weekly Education Sector Funding Trends Analysis",
    autosize=False,
    width=900,
    height=500,
    yaxis_range=[100, 130]
)

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/167_202312302255.png')
