import plotly.graph_objects as go
import pandas as pd

data = {
    'Date': ['2022-03-01', '2022-03-02', '2022-03-03', '2022-03-04', '2022-03-05',
             '2022-03-06', '2022-03-07', '2022-03-08', '2022-03-09', '2022-03-10',
             '2022-03-11', '2022-03-12', '2022-03-13', '2022-03-14'],
    'Open Price ($)': [120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185],
    'Close Price ($)': [123, 128, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190],
    'High Price ($)': [130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195],
    'Low Price ($)': [118, 122, 128, 134, 138, 143, 148, 153, 158, 163, 168, 173, 178, 183]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

fig.update_layout(title='March 2022 Daily Stock Prices in Technology Sector',
                  width=800,
                  height=600,
                  yaxis_range=[110, 200],
                  title_x=0.5)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/94_202312302255.png')