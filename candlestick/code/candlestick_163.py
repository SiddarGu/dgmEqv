import plotly.graph_objects as go
import pandas as pd

data = {'Date': ['2019-01-01', '2019-02-01', '2019-03-01', '2019-04-01', '2019-05-01', '2019-06-01', '2019-07-01', '2019-08-01', '2019-09-01', '2019-10-01', '2019-11-01', '2019-12-01', '2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01'],
        'Opening Price ($)': [120, 123, 127, 132, 135, 138, 142, 145, 148, 152, 155, 158, 162, 165, 168, 172],
        'Closing Price ($)': [122, 125, 130, 135, 138, 141, 145, 148, 151, 155, 158, 161, 165, 168, 171, 175],
        'High Price ($)': [125, 128, 135, 140, 143, 146, 150, 153, 156, 160, 163, 166, 170, 173, 176, 180],
        'Low Price ($)': [115, 120, 125, 130, 133, 136, 140, 143, 146, 150, 153, 156, 160, 163, 166, 170]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Closing Price ($)'])])

fig.update_layout(
    title='Monthly Stock Price Fluctuation in the Legal Industry',
    width=800,
    height=600,
    yaxis_range=[110, 190],
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=3,
                     label='3m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                     label='1y',
                     step='year',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type='date'
    )
)

fig.update_layout(
    autosize=False,
    width=800,
    height=600,
    margin=dict(l=40, r=40, t=40, b=40)
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/194_202312302255.png')
