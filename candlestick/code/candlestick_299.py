import plotly.graph_objects as go
import pandas as pd

data = {'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05', '2021-01-06', '2021-01-07', '2021-01-08'],
        'Open Price': [120, 125.5, 130, 135, 140, 145, 150, 155],
        'Close Price': [125.2, 130, 135, 140, 145, 150, 155, 160],
        'High Price': [130, 135, 140, 145, 150, 155, 160, 165],
        'Low Price': [115, 120, 125, 130, 135, 140, 145, 150]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price'],
                high=df['High Price'],
                low=df['Low Price'],
                close=df['Close Price'])])

fig.update_layout(
    title="Education Sector Stock Performance - First Week of January 2021",
    width=800,
    height=600,
    yaxis_range=[110, 170],
    autosize=False,
    margin=dict(l=50, r=50, b=50, t=50, pad=4),
    paper_bgcolor="white",
    plot_bgcolor="white"
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/161_202312302255.png')