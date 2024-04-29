import plotly.graph_objects as go
import pandas as pd

# Data
data = {'Date': ['2019-05-01', '2019-05-08', '2019-05-15', '2019-05-22', '2019-05-29', '2019-06-05', '2019-06-12', '2019-06-19', '2019-06-26'],
        'Open($)': [120, 115, 118, 122, 125, 128, 132, 136, 140],
        'Close($)': [115, 117, 120, 124, 127, 130, 134, 138, 142],
        'High($)': [122, 125, 130, 132, 135, 138, 140, 142, 144],
        'Low($)': [110, 112, 115, 119, 122, 125, 128, 132, 136]}

df = pd.DataFrame(data)

# Candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open($)'],
                close=df['Close($)'],
                high=df['High($)'],
                low=df['Low($)'])])

# Layout settings
fig.update_layout(title='Humanities and Social Sciences Publications Stock Performance - May to June Overview',
                  width=800,
                  height=600,
                  autosize=False,
                  margin=dict(l=30, r=30, b=30, t=100),
                  paper_bgcolor='rgb(255,255,255)',
                  plot_bgcolor='rgb(243,243,243)',
                  yaxis_range=[100, 150],
                  font=dict(family='Arial', size=12, color='rgb(0,0,0)'))

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/51_202312302255.png')