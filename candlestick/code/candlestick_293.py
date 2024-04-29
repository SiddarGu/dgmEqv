import pandas as pd
import plotly.graph_objects as go

data = {'Date': ['2019-01-01', '2019-01-08', '2019-01-15', '2019-01-22', '2019-01-29', '2019-02-05', '2019-02-12', '2019-02-19', '2019-02-26', '2019-03-05', '2019-03-12', '2019-03-19', '2019-03-26', '2019-04-02', '2019-04-09', '2019-04-16', '2019-04-23', '2019-04-30', '2019-05-07', '2019-05-14'],
        'Opening Price': [204, 217, 225, 231, 242, 252, 263, 276, 286, 296, 306, 316, 326, 336, 346, 356, 366, 376, 386, 396],
        'Buyout Price': [216, 224, 230, 240, 250, 262, 275, 285, 295, 305, 315, 325, 335, 345, 355, 365, 375, 385, 395, 405],
        'High Price': [218, 228, 235, 245, 253, 267, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410],
        'Low Price': [200, 213, 220, 225, 238, 248, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Opening Price'],
                                     high=df['High Price'],
                                     low=df['Low Price'],
                                     close=df['Buyout Price']
                                     )])

fig.update_layout(
    title='Financial Performance of Leading Employee Management Firm',
    width=1000,
    height=800,
    xaxis=dict(
        title='Date'
    ),
    yaxis=dict(
        title='Price',
        range=[min(df['Low Price'])-10, max(df['High Price'])+10]
    ),
)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/80_202312302255.png')
