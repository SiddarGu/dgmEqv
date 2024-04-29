import pandas as pd
import plotly.graph_objects as go

# Data
data = {'Date': ['2020-01-10', '2020-02-10', '2020-03-10', '2020-04-10', '2020-05-10', '2020-06-10', '2020-07-10', '2020-08-10', '2020-09-10', '2020-10-10', '2020-11-10', '2020-12-10', '2021-01-10', '2021-02-10', '2021-03-10', '2021-04-10', '2021-05-10', '2021-06-10', '2021-07-10'],
        'Open Price ($)': [120000, 127000, 131000, 130000, 135000, 139000, 145000, 150000, 157000, 163000, 166000, 170000, 175000, 180000, 185000, 192000, 195000, 200000, 204000],
        'Close Price ($)': [125000, 129000, 130000, 132500, 138000, 143000, 147000, 155000, 160000, 164000, 169000, 173000, 178000, 185000, 189000, 193000, 199000, 203000, 207000],
        'High Price ($)': [130000, 135000, 140000, 142000, 145000, 150000, 155000, 165000, 170000, 172000, 175000, 180000, 185000, 190000, 195000, 200000, 205000, 210000, 213000],
        'Low Price ($)': [115000, 120000, 125000, 128000, 131000, 135000, 140000, 145000, 152000, 155000, 160000, 165000, 170000, 175000, 180000, 187000, 190000, 195000, 200000]}

df = pd.DataFrame(data)

# Create figure
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

# Update layout
fig.update_layout(title='Monthly Price Trends in Real Estate and Housing Market 2020-2021',
                  width=1000,
                  height=600,
                  xaxis_rangeslider_visible=False,
                  yaxis_range=[min(df['Low Price ($)']) * 0.95, max(df['High Price ($)']) * 1.05])

# Save image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/71_202312302255.png')