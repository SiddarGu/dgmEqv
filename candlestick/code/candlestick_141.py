import plotly.graph_objects as go
import pandas as pd

# Create data dataframe
data = {'Date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01', '2020-10-01', '2020-11-01', '2020-12-01'],
        'Opening Price ($)': [20, 23, 25, 26, 27, 30, 31, 34, 35, 37, 38, 40],
        'Closing Price ($)': [22.5, 25, 27, 28, 30, 32, 33, 35, 36, 39, 40, 42],
        'High Price ($)': [23, 26, 28, 30, 32, 34, 35, 37, 38, 41, 42, 44],
        'Low Price ($)': [18, 21, 24, 25, 26, 28, 29, 32, 33, 35, 36, 38]}
df = pd.DataFrame(data)

# Create figure
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Opening Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Closing Price ($)'])])

# Update layout
fig.update_layout(
    title="Manufacturing and Production Industry: Yearly Stock Overview",
    width=1000,
    height=500,
    yaxis_range=[min(df['Low Price ($)'])-1, max(df['High Price ($)'])+1],
    margin=dict(l=50, r=50, t=50, b=50),
    showlegend=False,
    xaxis_rangeslider_visible=False,
    xaxis=dict(title="Date"),
    yaxis=dict(title="Price ($)"),
    font=dict(family="sans-serif")
)

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/210_202312302255.png')