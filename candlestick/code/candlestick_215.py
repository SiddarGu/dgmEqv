
import plotly.graph_objects as go
import pandas as pd

# Create dataframe
df = pd.DataFrame({'Date':['2020-08-08', '2020-08-15', '2020-08-22', '2020-08-29', '2020-09-05', '2020-09-12', '2020-09-19', '2020-09-26'], 
                   'Opening Price ($)':[3.5, 3.3, 2.9, 3.2, 3.5, 3.2, 3.6, 3.3],
                   'Closing Price ($)':[3.2, 2.7, 3.1, 3.7, 3.3, 3.6, 3.1, 3.4],
                   'High Price ($)':[3.9, 3.7, 3.7, 3.9, 3.8, 4, 3.8, 3.7],
                   'Low Price ($)':[2.9, 2.5, 2.7, 2.8, 2.9, 2.9, 2.8, 3.1]})

# Create figure
fig = go.Figure(data=[go.Candlestick(x=df['Date'], 
                         open=df['Opening Price ($)'], 
                         high=df['High Price ($)'], 
                         low=df['Low Price ($)'], 
                         close=df['Closing Price ($)'])])

# Update figure layout
fig.update_layout(title_text='Financial Trends in the Food and Beverage Industry',
                  width=500,
                  height=400,
                  yaxis_range=[2.5, 4])

# Save figure
fig.write_image(r'/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/14_202312270043.png')