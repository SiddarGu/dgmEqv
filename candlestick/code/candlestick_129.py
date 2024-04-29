import plotly.graph_objects as go

data = [
    {'Date': '2018-Q1', 'Open Budget (Billion $)': 650, 'Close Budget (Billion $)': 700, 'High Budget (Billion $)': 750, 'Low Budget (Billion $)': 640},
    {'Date': '2018-Q2', 'Open Budget (Billion $)': 690, 'Close Budget (Billion $)': 730, 'High Budget (Billion $)': 770, 'Low Budget (Billion $)': 680},
    {'Date': '2018-Q3', 'Open Budget (Billion $)': 750, 'Close Budget (Billion $)': 800, 'High Budget (Billion $)': 850, 'Low Budget (Billion $)': 720},
    {'Date': '2018-Q4', 'Open Budget (Billion $)': 720, 'Close Budget (Billion $)': 750, 'High Budget (Billion $)': 780, 'Low Budget (Billion $)': 700},
    {'Date': '2019-Q1', 'Open Budget (Billion $)': 770, 'Close Budget (Billion $)': 810, 'High Budget (Billion $)': 860, 'Low Budget (Billion $)': 760}
]

fig = go.Figure(data=[go.Candlestick(x=[d['Date'] for d in data],
                                     open=[d['Open Budget (Billion $)'] for d in data],
                                     close=[d['Close Budget (Billion $)'] for d in data],
                                     high=[d['High Budget (Billion $)'] for d in data],
                                     low=[d['Low Budget (Billion $)'] for d in data])])

fig.update_layout(title='Government Public Policy: Quarterly Budget Overview',
                  autosize=False,
                  width=800,
                  height=600,
                  yaxis_range=[600, 900])

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/204_202312302255.png')