import pandas as pd
import plotly.graph_objects as go

# Data
data = {'Date': ['2020-06-01', '2020-06-02', '2020-06-03', '2020-06-04', '2020-06-05', '2020-06-08', '2020-06-09', 
                 '2020-06-10', '2020-06-11', '2020-06-12', '2020-06-15', '2020-06-16', '2020-06-17', '2020-06-18', 
                 '2020-06-19'],
        'Opening Price ($)': [70, 72, 73, 72, 75, 77, 76, 79, 82, 84, 86, 88, 92, 94, 96],
        'Closing Price ($)': [72, 73, 72, 74, 76, 76, 78, 82, 83, 85, 87, 90, 93, 95, 97],
        'High Price ($)': [75, 76, 76, 77, 78, 80, 82, 85, 86, 88, 89, 94, 95, 99, 101],
        'Low Price ($)': [68, 69, 70, 71, 73, 74, 75, 79, 81, 82, 85, 88, 90, 93, 95]}

df = pd.DataFrame(data)

# Create Candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Opening Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Closing Price ($)'])])

# Set chart and text size
fig.update_layout(width=1000, height=700)
fig.update_layout(title='June 2020 Daily Price Range of Wheat in Agriculture and Food Production Sector',
                  font_size=10)

# Set y-axis range
yaxis_range = [df['Low Price ($)'].min() - 5, df['High Price ($)'].max() + 5]
fig.update_layout(yaxis_range=yaxis_range)

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/91_202312302255.png')