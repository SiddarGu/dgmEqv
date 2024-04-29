import plotly.graph_objects as go
import pandas as pd

data = {'Date': ['2021-10-20', '2021-10-21', '2021-10-22', '2021-10-25', '2021-10-26', '2021-10-27', '2021-10-28', '2021-10-29', '2021-10-30', '2021-11-02', '2021-11-03', '2021-11-04', '2021-11-05', '2021-11-06', '2021-11-09', '2021-11-10', '2021-11-11', '2021-11-12', '2021-11-13', '2021-11-16'],
        'Open Price': [122.5, 126, 130, 132.2, 130, 134, 138, 143, 146, 150, 152, 154, 158, 161, 164, 167, 169, 171, 175, 177],
        'Closed Price': [124.7, 128.6, 131.5, 130.9, 131.2, 137, 139.5, 145, 148, 151, 153, 155, 160, 163, 166, 168, 170, 173, 176, 178],
        'High Price': [125.5, 130, 132, 133.5, 132.4, 139, 140.2, 149, 152, 153, 156, 157, 163, 165, 168, 172, 174, 175, 178, 180],
        'Low Price': [120.2, 125, 128, 127.4, 127, 133, 135, 140, 145, 147, 150, 152, 156, 159, 160, 165, 166, 170, 172, 175]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price'],
                high=df['High Price'],
                low=df['Low Price'],
                close=df['Closed Price'])])

fig.update_layout(title='Historical Stock Prices of Major Companies in the Food and Beverage Industry 2021',
                  width=800,
                  height=600,
                  autosize=False,
                  margin=dict(l=50, r=50, b=100, t=100, pad=4),
                  yaxis_range=[100, 200])

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/226_202312302255.png')