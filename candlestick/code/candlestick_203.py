import pandas as pd
import plotly.graph_objects as go

data = {
    'Date': ['2022-01-01', '2022-01-08', '2022-01-15', '2022-01-22', '2022-01-29',
             '2022-02-05', '2022-02-12', '2022-02-19', '2022-02-26', '2022-03-05',
             '2022-03-12', '2022-03-19', '2022-03-26', '2022-04-02', '2022-04-09',
             '2022-04-16', '2022-04-23', '2022-04-30'],
    'Open Price ($)': [100, 105, 108, 111, 115, 117, 120, 122, 124, 126, 129, 131, 134, 137, 141, 143, 146, 149],
    'Close Price ($)': [105, 107, 111, 114, 116, 119, 122, 123, 125, 128, 130, 134, 136, 139, 142, 146, 148, 151],
    'High Price ($)': [110, 112, 115, 120, 121, 123, 126, 128, 129, 132, 135, 139, 141, 144, 147, 151, 153, 156],
    'Low Price ($)': [90, 102, 106, 110, 113, 115, 118, 121, 123, 125, 127, 130, 133, 136, 140, 142, 145, 148]
}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     close=df['Close Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'])])

fig.update_layout(
    title="Manufacturing and Production Sector Financial Trend Analysis",
    width=800,
    height=600,
    xaxis=dict(
        autorange=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(visible=False),
        type="date"
    ),
    yaxis=dict(
        autorange=True,
        rangemode='nonnegative',
        title='Price ($)'
    ),
    yaxis2=dict(
        autorange=True,
        rangemode='nonnegative',
        title='Price ($)'
    ),
    yaxis3=dict(
        autorange=True,
        rangemode='nonnegative',
        title='Price ($)'
    ),
    yaxis4=dict(
        autorange=True,
        rangemode='nonnegative',
        title='Price ($)'
    ),
    yaxis5=dict(
        autorange=True,
        rangemode='nonnegative',
        title='Price ($)'
    )
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/147_202312302255.png')
