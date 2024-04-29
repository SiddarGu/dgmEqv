import plotly.graph_objects as go
import pandas as pd

# Define data
data = {
    'Date': ['2021-01-04', '2021-01-11', '2021-01-18', '2021-01-25', '2021-02-01', '2021-02-08', '2021-02-15', '2021-02-22', '2021-03-01', '2021-03-08'],
    'Open Price ($)': [1000, 1025, 1045, 1085, 1095, 1092, 1125, 1150, 1170, 1187],
    'Close Price ($)': [1020, 1040, 1080, 1100, 1090, 1120, 1145, 1165, 1185, 1220],
    'High Price ($)': [1050, 1065, 1100, 1120, 1125, 1140, 1170, 1190, 1210, 1245],
    'Low Price ($)': [990, 1010, 1030, 1075, 1080, 1085, 1110, 1135, 1155, 1180]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create Candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

# Set chart title
fig.update_layout(title='Weekly Government Bond Trends in 2021',
                  width=1000,
                  height=500)

# Set y-axis range
fig.update_layout(yaxis_range=(df['Low Price ($)'].min() - 50, df['High Price ($)'].max() + 50))

# Save figure as image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/104_202312302255.png')