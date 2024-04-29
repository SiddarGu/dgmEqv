import pandas as pd
import plotly.graph_objects as go

# Data
data = {'Date': ['2020-10-01', '2020-10-02', '2020-10-03', '2020-10-04', '2020-10-05', '2020-10-06', '2020-10-07', '2020-10-08', '2020-10-09', '2020-10-10', '2020-10-11', '2020-10-12'],
        'Open Price ($)': [350, 372, 375, 380, 390, 412, 460, 472, 495, 510, 515, 540],
        'Close Price ($)': [370, 375, 378, 390, 410, 450, 470, 490, 510, 530, 540, 560],
        'High Price ($)': [375, 380, 385, 400, 415, 460, 480, 500, 520, 540, 550, 570],
        'Low Price ($)': [345, 367, 372, 375, 385, 410, 450, 467, 490, 505, 510, 530]}

df = pd.DataFrame(data)

# Plotly Candlestick Chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Open Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'],
                                     close=df['Close Price ($)'])])

# Layout
fig.update_layout(title='Engineering Firm Share Price Trend in October 2020',
                  width=800,
                  height=600,
                  xaxis_rangeslider_visible=False,
                  xaxis=dict(tickangle=45),
                  yaxis_range=[300, 600],
                  showlegend=False)

# Save image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/89_202312302255.png')