import plotly.graph_objects as go

# Data
data = [['2019-06-01', 1200, 1250, 1300, 1150],
        ['2019-06-08', 1300, 1350, 1400, 1280],
        ['2019-06-15', 1360, 1380, 1450, 1290],
        ['2019-06-22', 1400, 1450, 1500, 1350],
        ['2019-06-29', 1480, 1520, 1600, 1400],
        ['2019-07-06', 1500, 1550, 1600, 1450],
        ['2019-07-13', 1570, 1600, 1650, 1550],
        ['2019-07-20', 1620, 1650, 1700, 1600],
        ['2019-07-27', 1700, 1800, 1850, 1650]]

# Extracting data
dates = [row[0] for row in data]
opening_prices = [row[1] for row in data]
closing_prices = [row[2] for row in data]
high_prices = [row[3] for row in data]
low_prices = [row[4] for row in data]

# Candlestick chart
fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=opening_prices, 
                                     close=closing_prices,
                                     high=high_prices,
                                     low=low_prices)])

# Figure layout
fig.update_layout(title='Art Works Auction Market Trend 2019',
                  width=800, 
                  height=600,
                  yaxis_range=[min(low_prices)-50, max(high_prices)+50],
                  showlegend=False,
                  template='plotly_white')

# Saving the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/127_202312302255.png')