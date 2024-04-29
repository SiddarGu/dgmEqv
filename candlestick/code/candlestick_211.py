import pandas as pd
import plotly.graph_objects as go

# Initialize the data
data = {'Date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01'],
        'Open Price ($)': [550000, 565000, 560000, 540000, 530000, 550000, 540000, 535000],
        'Close Price ($)': [545000, 565000, 552000, 535000, 530000, 540000, 540000, 525000],
        'High Price ($)': [555000, 570000, 565000, 555000, 540000, 560000, 550000, 540000],
        'Low Price ($)': [540000, 560000, 545000, 530000, 525000, 535000, 530000, 500000]}

# Create a DataFrame
df = pd.DataFrame(data)

# Convert Date column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Create a candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     close=df['Close Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'])])

# Update the layout
fig.update_layout(
    title='Monthly Housing Market Trends 2020',
    width=800,
    height=600,
    xaxis_range=[df['Date'].min(), df['Date'].max()],
    yaxis_range=[df[['Open Price ($)', 'Close Price ($)', 'High Price ($)', 'Low Price ($)']].values.min(),
                 df[['Open Price ($)', 'Close Price ($)', 'High Price ($)', 'Low Price ($)']].values.max()],
    font=dict(),
    showlegend=False
)

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/79_202312302255.png', width=800, height=600)