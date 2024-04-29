import plotly.graph_objects as go
import pandas as pd

# Define the data
data = {'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08', '2022-01-09'],
        'Open Price ($)': [120, 122, 123, 125, 127, 129, 132, 134, 136],
        'Close Price ($)': [122.5, 124, 125.5, 127, 129.5, 132, 134.5, 136.5, 138],
        'High Price ($)': [124, 125, 127, 128.5, 131, 134, 136, 138, 140],
        'Low Price ($)': [118, 120, 121, 123, 125, 128, 130, 132, 134]}

# Create DataFrame from the data
df = pd.DataFrame(data)

# Convert the Date column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Create the candlestick chart
fig = go.Figure(data=go.Candlestick(x=df['Date'],
                    open=df['Open Price ($)'],
                    high=df['High Price ($)'],
                    low=df['Low Price ($)'],
                    close=df['Close Price ($)']))

# Set the title
fig.update_layout(title='Tech Stock Prices Trend in the first week of January 2022')

# Set the size parameters
fig.update_layout(width=800, height=600)
fig.update_layout(autosize=False, margin=dict(l=20, r=20, t=40, b=40))
fig.update_layout(yaxis_range=[115, 145])

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/61_202312302255.png')