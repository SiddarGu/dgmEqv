import plotly.graph_objects as go
import pandas as pd

data = {
    'Date': ['2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05'],
    'Opening Price ($)': [120, 130, 140, 150, 160],
    'Closing Price ($)': [130, 140, 150, 160, 170],
    'High Price ($)': [135, 145, 155, 165, 175],
    'Low Price ($)': [115, 125, 135, 145, 155]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])

fig.update_layout(title='Litigation Financing Firm Stock Performance - 5 Days Overview')
fig.update_layout(width=800, height=600)
fig.update_layout(xaxis_rangeslider_visible=False)
fig.update_yaxes(automargin=True)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/63_202312302255.png')