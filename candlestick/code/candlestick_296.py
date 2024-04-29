import pandas as pd
import plotly.graph_objects as go

# Data
data = {
    'Date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08', '2020-01-09', '2020-01-10', '2020-01-11', '2020-01-12', '2020-01-13', '2020-01-14', '2020-01-15', '2020-01-16', '2020-01-17', '2020-01-18', '2020-01-19'],
    'Open Price ($)': [42, 43.5, 44, 45, 46.5, 47, 48, 49.5, 50, 51.5, 52, 53, 54, 55.5, 56, 57, 58, 59.5, 60],
    'Close Price ($)': [43.5, 44, 45, 46.5, 47, 48, 49.5, 50, 51.5, 52, 53, 54, 55.5, 56, 57, 58, 59.5, 60, 61.5],
    'High Price ($)': [45, 46.2, 47, 48.5, 50, 51, 52, 53, 54.5, 55, 56.2, 57, 58, 59, 60, 61, 62, 63, 64],
    'Low Price ($)': [40, 41.9, 42, 43.2, 44, 45, 46.5, 47, 48, 49, 50, 51, 52, 52.5, 53.5, 54, 55.3, 56, 57]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create Candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                    open=df['Open Price ($)'],
                                    high=df['High Price ($)'],
                                    low=df['Low Price ($)'],
                                    close=df['Close Price ($)'])])

# Update layout
fig.update_layout(title={'text': 'Energy and Utilities Sector: Daily Opening, Closing, High, and Low Prices in January 2020',
                         'y': 0.95,
                         'x': 0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'},
                  width=800,
                  height=600,
                  margin=dict(l=50, r=50, b=50, t=80),
                  yaxis_range=[min(df['Low Price ($)'])-2, max(df['High Price ($)'])+2],
                  showlegend=False)

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/73_202312302255.png')