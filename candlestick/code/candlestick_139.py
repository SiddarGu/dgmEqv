import pandas as pd
import plotly.graph_objects as go

# Data
data = {'Date':['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01', '2020-10-01', '2020-11-01', '2020-12-01'],
        'Open Price (Million $)':[140, 150, 145, 155, 165, 170, 180, 190, 200, 210, 215, 210],
        'Close Price (Million $)':[150, 145, 155, 165, 170, 180, 190, 200, 210, 215, 210, 220],
        'High Price (Million $)':[155, 155, 160, 170, 175, 185, 195, 205, 215, 220, 220, 225],
        'Low Price (Million $)':[135, 140, 140, 150, 160, 170, 180, 185, 195, 205, 200, 205]}

df = pd.DataFrame(data)

# Candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price (Million $)'],
                high=df['High Price (Million $)'],
                low=df['Low Price (Million $)'],
                close=df['Close Price (Million $)'])])

# Layout
fig.update_layout(
    title='Monthly Finance Trend in the Education Sector',
    width=800,
    height=600,
    yaxis_range=[100, 250],
    showlegend=False,
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(visible=False),
        type="date"
    ),
    yaxis=dict(domain=[0, 0.8]),
    yaxis2=dict(domain=[0.8, 1])
)

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/133_202312302255.png')