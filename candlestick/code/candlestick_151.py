import plotly.graph_objects as go
import pandas as pd

# Create data
data = {'Date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08', '2020-01-09', '2020-01-10'],
        'Open Price (Twitter)': [30.50, 32.50, 34.00, 33.25, 32.00, 35.50, 36.75, 38.00, 39.00, 44.00],
        'Close Price (Twitter)': [32.00, 33.20, 32.90, 31.90, 34.80, 37.70, 38.50, 40.30, 43.90, 42.90],
        'High Price (Twitter)': [34.80, 35.00, 36.50, 33.70, 36.20, 39.00, 40.60, 41.00, 45.20, 47.00],
        'Low Price (Twitter)': [29.20, 31.10, 32.00, 30.90, 31.50, 34.20, 33.20, 35.70, 37.90, 39.50]}

df = pd.DataFrame(data)

# Create Candlestick plot
fig = go.Figure(data=go.Candlestick(x=df['Date'],
                open=df['Open Price (Twitter)'],
                high=df['High Price (Twitter)'],
                low=df['Low Price (Twitter)'],
                close=df['Close Price (Twitter)']))

# Set figure title
fig.update_layout(title="Twitter's Stock Performance in the First 10 Days of January 2020")

# Set figure size parameters
fig.update_layout(
    autosize=False,
    width=800,
    height=600,
    margin=dict(l=40, r=40, t=40, b=40),
    paper_bgcolor="white",
)

# Adjust yaxis range
fig.update_layout(yaxis_range=[df['Low Price (Twitter)'].min()-1, df['High Price (Twitter)'].max()+1])

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/66_202312302255.png')