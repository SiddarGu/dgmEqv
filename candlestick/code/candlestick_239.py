
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

# Create data frame
data = {'Date': ['2019-05-01', '2019-05-02', '2019-05-03', '2019-05-04', '2019-05-05', '2019-05-06', '2019-05-07'],
        'Opening Price ($)': [50.2, 47.5, 49.2, 50.6, 51.7, 53.3, 54.2],
        'Closing Price ($)': [48, 48.8, 50.6, 51.7, 53.3, 54.2, 55.2],
        'High Price ($)': [54.5, 51.3, 52.0, 54.2, 55.7, 56.2, 57.1],
        'Low Price ($)': [46.2, 45.3, 47.1, 49.1, 50.1, 51.3, 52.5]
        }

df = pd.DataFrame(data)

# Create figure
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                       open=df['Opening Price ($)'],
                       high=df['High Price ($)'],
                       low=df['Low Price ($)'],
                       close=df['Closing Price ($)'])])

# Update figure
fig.update_layout(title='Financial Trend in Manufacturing and Production Industry - Weekly Overview',
                  xaxis_title='Date',
                  yaxis_title='Stock Price ($)',
                  yaxis_range=[min(df['Low Price ($)'])-2, max(df['High Price ($)'])+2],
                  width=800,
                  height=500,
                  font=dict(size=8))

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/49_202312252244.png')