import pandas as pd
import plotly.graph_objects as go

# Create the data
data = {'Date': ['2020-10-12', '2020-10-13', '2020-10-14', '2020-10-15', '2020-10-16', '2020-10-19', '2020-10-20', '2020-10-21', '2020-10-22', '2020-10-23', '2020-10-26', '2020-10-27', '2020-10-28', '2020-10-29', '2020-10-30'],
        'Open Price': [107, 109, 112, 104, 105, 116, 121, 123, 122, 121, 114, 113, 115, 117, 114],
        'Close Price': [110, 111, 102, 105, 115, 120, 123, 122, 120, 116, 113, 114, 116, 115, 112],
        'High Price': [113, 114, 113, 107, 116, 124, 125, 126, 124, 122, 116, 117, 120, 119, 118],
        'Low Price': [102, 108, 100, 101, 104, 116, 119, 121, 118, 115, 111, 112, 114, 114, 106]
        }

df = pd.DataFrame(data)

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price'],
                                     high=df['High Price'],
                                     low=df['Low Price'],
                                     close=df['Close Price'])])

# Update layout
fig.update_layout(
    title='Law Firms Profit Margins Over Time',
    width=1000,
    height=500,
    xaxis=dict(
        rangeslider=dict(
            visible=False
        ),
        type='category'
    ),
    yaxis=dict(
        autorange=True,
    ),
    showlegend=False
)

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/189_202312302255.png')