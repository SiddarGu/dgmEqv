import plotly.graph_objects as go
import pandas as pd

# Create dataframe from data
data = {'Date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01'],
        'Open Price($)': [250000, 260000, 270000, 265000, 280000, 295000],
        'Close Price($)': [255000, 270000, 265000, 280000, 295000, 300000],
        'High Price($)': [260000, 280000, 275000, 290000, 300000, 305000],
        'Low Price($)': [248000, 255000, 260000, 260000, 275000, 280000]}

df = pd.DataFrame(data)

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price($)'],
                                     close=df['Close Price($)'],
                                     high=df['High Price($)'],
                                     low=df['Low Price($)'])])

# Set title
fig.update_layout(title='Monthly Real Estate Prices in Housing Market')

# Set size parameters
fig.update_layout(width=800, height=600, showlegend=False)

# Set yaxis range
fig.update_layout(yaxis_range=[min(df['Low Price($)']) - 10000, max(df['High Price($)']) + 10000])

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/162_202312302255.png')