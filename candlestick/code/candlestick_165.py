import plotly.graph_objects as go
import pandas as pd

data = {"Date": ["2018-04-27", "2018-04-28", "2018-04-29", "2018-04-30", "2018-05-01", "2018-05-02", "2018-05-03", "2018-05-04", "2018-05-05", "2018-05-06"],
        "Opening Price ($)": [45.5, 48.5, 48.8, 49.3, 50.6, 51.2, 53.7, 53.0, 56.2, 57.4],
        "Closing Price ($)": [48.5, 48.8, 49.3, 50.6, 51.2, 53.7, 53.0, 56.2, 57.4, 58.6],
        "High Price ($)": [50.2, 51.1, 51.7, 52.4, 53.3, 54.8, 55.6, 58.9, 59.9, 60.5],
        "Low Price ($)": [43, 46, 47.5, 48, 49.4, 50.7, 52.8, 52, 54.1, 55.9]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Opening Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Closing Price ($)'])])

fig.update_layout(title='Logistics Company Stock Trend in the First Week of May 2018',
                  xaxis_title='Date',
                  yaxis_title='Price ($)',
                  yaxis_range=[min(df['Low Price ($)']) - 2, max(df['High Price ($)']) + 2],
                  width=800,
                  height=600)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/186_202312302255.png')