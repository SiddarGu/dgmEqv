import pandas as pd
import plotly.graph_objects as go

# Define the data
data = {'Date': ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05',
                 '2020-01-06', '2020-01-07', '2020-01-08', '2020-01-09', '2020-01-10',
                 '2020-01-11', '2020-01-12', '2020-01-13', '2020-01-14', '2020-01-15'],
        'Open Price ($)': [20, 22.6, 22, 22, 23.5, 24, 26.5, 26, 27.5, 27, 29.5, 29, 31.5, 31, 33.5],
        'Close Price ($)': [22.5, 22, 21.5, 23.5, 24, 26.5, 26, 27.5, 27, 29.5, 29, 31.5, 31, 33.5, 33],
        'High Price ($)': [23, 23.5, 23, 24, 25, 27, 27.5, 28, 28.5, 30, 30.5, 32, 32.5, 34, 34.5],
        'Low Price ($)': [19, 22, 20.5, 21, 23, 24, 26, 25.5, 27, 27, 29, 29, 31, 31, 33]
       }

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Configure the figure
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

fig.update_layout(title='Manufacturing and Production Sector Stock Performance - 15 Day Overview',
                  width=1200,
                  height=800,
                  yaxis_range=[min(df['Low Price ($)']) - 1, max(df['High Price ($)']) + 1],
                  template='plotly_white')

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/98_202312302255.png')