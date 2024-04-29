import plotly.graph_objects as go
import pandas as pd

# Define data
data = {'Date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08'],
        'Opening Price': [125.6, 130, 140, 139, 145, 152, 160, 168],
        'Closing Price': [130, 135, 137, 143, 150, 157, 167, 176],
        'High Price': [132, 140, 150, 147, 155, 162, 170, 180],
        'Low Price': [120, 130, 134, 139, 145, 151, 159, 168]}

# Create dataframe
df = pd.DataFrame(data)

# Create candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price'],
                high=df['High Price'],
                low=df['Low Price'],
                close=df['Closing Price'])])

# Set title
fig.update_layout(title='Weekly Trend of Legal Services Stock Price')

# Set size
fig.update_layout(
    width=1000,
    height=600,
    autosize=False
)

# Set yaxis range
fig.update_yaxes(range=[min(df['Low Price'])-5, max(df['High Price'])+5])

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/53_202312302255.png')