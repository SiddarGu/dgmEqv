import plotly.graph_objects as go
import pandas as pd

# Data
data = {'Date': ['2020-06-01', '2020-06-02', '2020-06-03', '2020-06-04', '2020-06-05'],
        'Open price ($)': [100, 102, 109, 110, 113],
        'Close price ($)': [102, 105, 110, 113, 112],
        'High price ($)': [105, 110, 115, 118, 120],
        'Low price ($)': [99, 100, 107, 107, 108]}
df = pd.DataFrame(data)

# Create Candlestick Chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open price ($)'],
                high=df['High price ($)'],
                low=df['Low price ($)'],
                close=df['Close price ($)'])])

# Update Layout
fig.update_layout(title='Corporate bond weekly prices',
                  xaxis_title='Date',
                  yaxis_title='Price ($)',
                  width=800,
                  height=600,
                  yaxis_range=[min(df['Low price ($)'])-5, max(df['High price ($)'])+5])

# Save the Figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/184_202312302255.png')