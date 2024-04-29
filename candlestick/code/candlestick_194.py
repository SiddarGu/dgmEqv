import pandas as pd
import plotly.graph_objects as go

data = {'Date': ['2020-01-06', '2020-01-13', '2020-01-20', '2020-01-27', '2020-02-03', '2020-02-10',
                 '2020-02-17', '2020-02-24', '2020-03-02', '2020-03-09'],
        'Open Price ($)': [230, 235, 242, 243, 245, 248, 250, 252, 255, 260],
        'Close Price ($)': [235, 242, 243, 245, 248, 250, 252, 255, 260, 265],
        'High Price ($)': [238, 245, 245, 248, 250, 252, 254, 258, 265, 270],
        'Low Price ($)': [227, 232, 239, 240, 242, 245, 248, 250, 252, 255]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Close Price ($)'])])

fig.update_layout(
    title='Investing Trends in Tech-Engineering Firms',
    width=1000,
    height=600,
    font_family='sans-serif',
    yaxis_range=[min(df['Low Price ($)'])-5, max(df['High Price ($)'])+5]
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/181_202312302255.png')