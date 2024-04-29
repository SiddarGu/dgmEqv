import plotly.graph_objects as go
import pandas as pd

data = {'Date': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01', '2021-07-01', '2021-08-01', '2021-09-01', '2021-10-01', '2021-11-01', '2021-12-01'],
        'Opening Donation ($)': [5000, 5500, 6000, 6500, 6800, 7000, 7500, 7800, 8100, 8400, 8800, 9100],
        'Closing Donation ($)': [5200, 5600, 6100, 6700, 6900, 7300, 7600, 8000, 8300, 8700, 9000, 9300],
        'High Donation ($)': [5700, 6000, 6600, 7100, 7400, 7700, 8100, 8500, 8800, 9200, 9500, 9800],
        'Low Donation ($)': [4800, 5000, 5900, 6300, 6600, 6800, 7300, 7500, 7900, 8200, 8500, 8900]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Opening Donation ($)'],
                high=df['High Donation ($)'],
                low=df['Low Donation ($)'],
                close=df['Closing Donation ($)'])])

fig.update_layout(title='Monthly Donation Trends for Charity and Nonprofit Organizations-Nature of 2021',
                  width=800,
                  height=600,
                  yaxis_range=[min(df['Low Donation ($)']) - 200, max(df['High Donation ($)']) + 200],
                  margin=dict(l=50, r=50, t=50, b=50),
                  showlegend=False)

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/187_202312302255.png')