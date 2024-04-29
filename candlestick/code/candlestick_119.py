import plotly.graph_objects as go
import pandas as pd

# Create DataFrame
data = {'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07'],
        'Opening Price ($)': [40.2, 41.7, 42.5, 45.7, 47.4, 48.3, 49.6],
        'Closing Price ($)': [41.5, 42.3, 45.0, 47.0, 48.0, 49.5, 51.0],
        'High Price ($)': [42.8, 44.0, 46.3, 48.8, 49.8, 50.7, 52.3],
        'Low Price ($)': [39.9, 41.5, 42.0, 45.5, 46.9, 48.0, 49.3]}

df = pd.DataFrame(data)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create candlestick chart figure
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['Opening Price ($)'],
                    high=df['High Price ($)'],
                    low=df['Low Price ($)'],
                    close=df['Closing Price ($)'])])

# Update layout parameters
fig.update_layout(title='Entertainment Company Stock Performance - Week Overview',
                  width=900,
                  height=600,
                  xaxis_title='Date',
                  yaxis_title='Price ($)',
                  yaxis_range=[df['Low Price ($)'].min()-1, df['High Price ($)'].max()+1])

# Save figure as image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/87_202312302255.png')