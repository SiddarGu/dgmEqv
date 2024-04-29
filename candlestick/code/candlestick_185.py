
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Read in Data
data = [['2019-04-26', 50.2, 52.1, 53.4, 48.7],
        ['2019-04-27', 50.8, 51.2, 52.7, 49.3],
        ['2019-04-28', 51.3, 53.2, 53.4, 50.2],
        ['2019-04-29', 52.5, 54.9, 55.7, 52.1],
        ['2019-04-30', 54.2, 56.4, 57.9, 52.9],
        ['2019-05-01', 54.6, 55.2, 57.9, 54.1]]

df = pd.DataFrame(data, columns=['Date', 'Opening Price ($)', 'Closing Price ($)', 'High Price ($)', 'Low Price ($)'])

# Create figure
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Opening Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)'],
    close=df['Closing Price ($)']
)])

# Update figure
fig.update_layout(title={'text': 'Retail Company Stock Performance - One Month Overview',
                        'y': 0.9,
                        'x': 0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                  width=600,
                  height=400,
                  yaxis_range=[np.min(df[['Low Price ($)']]), np.max(df[['High Price ($)']])])

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/7_202312252244.png')