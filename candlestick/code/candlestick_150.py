import pandas as pd
import plotly.graph_objects as go

# Data
data = {
    'Date': ['2021-01-02', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-02', '2021-07-01', '2021-08-01', '2021-09-01', '2021-10-02', '2021-11-01', '2021-12-01', '2022-01-02', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01', '2022-06-02'],
    'Open Price ($)': [200, 215, 230, 255, 275, 310, 330, 345, 360, 375, 395, 405, 420, 435, 450, 465, 480, 495],
    'Close Price ($)': [220, 240, 250, 270, 300, 325, 350, 365, 380, 400, 410, 430, 440, 460, 480, 490, 500, 520],
    'High Price ($)': [225, 250, 260, 280, 310, 340, 360, 375, 390, 420, 425, 440, 455, 475, 495, 510, 520, 540],
    'Low Price ($)': [195, 200, 225, 240, 270, 290, 320, 335, 350, 370, 385, 400, 410, 425, 440, 455, 470, 485]
}

df = pd.DataFrame(data)

# Candlestick Chart
fig = go.Figure(data=[go.Candlestick(
    x=df['Date'],
    open=df['Open Price ($)'],
    close=df['Close Price ($)'],
    high=df['High Price ($)'],
    low=df['Low Price ($)']
)])
    
# Layout
fig.update_layout(
    title='Real Estate and Housing Market Trends (2021 - 2022): Opening, Closing, High and Low Prices',
    width=1000,
    height=600,
    yaxis_range=[100, 600],
    xaxis=dict(
        dtick="M1",
        tickformat="%Y-%m-%d"
    ),
    template='plotly_white'
)

# Save Figure
fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/141_202312302255.png")