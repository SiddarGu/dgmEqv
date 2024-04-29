import plotly.graph_objects as go

data = [['2021-12-01', 70.2, 75.8, 76.2, 69.3],
        ['2021-12-08', 75.1, 78, 79.5, 74.2],
        ['2021-12-15', 77.6, 80.2, 81.1, 76.9],
        ['2021-12-22', 80.5, 85, 86.5, 79.9],
        ['2021-12-29', 85.2, 86.7, 89.1, 84.1],
        ['2022-01-05', 87, 89.8, 90.2, 85.6],
        ['2022-01-12', 89.7, 93.1, 94, 88.5],
        ['2022-01-19', 93.5, 95.7, 97.1, 91.9]]

fig = go.Figure(data=[go.Candlestick(x=[row[0] for row in data],
                                    open=[row[1] for row in data],
                                    close=[row[2] for row in data],
                                    high=[row[3] for row in data],
                                    low=[row[4] for row in data])])

fig.update_layout(title="December 2021 to January 2022 Stock Prices in Food and Beverage Industry",
                  width=800,
                  height=600,
                  yaxis_range=[min([row[4] for row in data]) - 1, max([row[3] for row in data]) + 1])

fig.update_layout(font=dict(family="sans-serif"))

fig.update_layout(autosize=False)

fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/135_202312302255.png')