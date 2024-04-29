import plotly.graph_objects as go

data = {'Date': ['2022-08-01', '2022-08-02', '2022-08-03', '2022-08-04', '2022-08-05', '2022-08-06', '2022-08-07', '2022-08-08'],
        'Open Price ($/Barrel)': [70, 70.4, 66, 68, 67.8, 68.6, 68.4, 68.2],
        'Close Price ($/Barrel)': [72.2, 68.5, 67.6, 70.4, 69.4, 70, 69.2, 70],
        'High Price ($/Barrel)': [74.5, 72.1, 69.2, 72.6, 71, 72.4, 70.8, 72.2],
        'Low Price ($/Barrel)': [68.6, 67.8, 64.1, 65.9, 66.2, 67.2, 66.6, 66.8]}

fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                                    open=data['Open Price ($/Barrel)'],
                                    close=data['Close Price ($/Barrel)'],
                                    high=data['High Price ($/Barrel)'],
                                    low=data['Low Price ($/Barrel)'])])

fig.update_layout(title='Daily Oil Prices in Energy and Utilities Industry',
                  width=800,
                  height=600,
                  yaxis_range=[60, 80])

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/62_202312302255.png')