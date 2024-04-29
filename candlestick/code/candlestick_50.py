
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Create Data
data = {'Date': ['2019-04-26','2019-04-27','2019-04-28','2019-04-29','2019-04-30','2019-05-01','2019-05-02','2019-05-03'],
        'Opening Price ($)': [120.5,123,125,126,127,128,129,130],
        'Closing Price ($)': [122,122.1,124,127.7,128.9,130,130,131],
        'High Price ($)': [126.2,125.2,125,129.6,130.2,132,134,134],
        'Low Price ($)': [119.8,121.9,121.7,125.4,127.6,125.8,127.9,128]}

# Create Dataframe
df = pd.DataFrame(data)

# Plot Candlestick Chart
fig = make_subplots(rows=1, cols=1, shared_xaxes=True)
fig.add_trace(go.Candlestick(x=df['Date'],
                              open=df['Opening Price ($)'],
                              high=df['High Price ($)'],
                              low=df['Low Price ($)'],
                              close=df['Closing Price ($)']), row=1, col=1)

# Adjust Figure Layout
fig.update_layout(title='Technology and the Internet Stock Performance Overview',
                  width=1000, height=600,
                  yaxis_range=[min(df['Low Price ($)'])-2, max(df['High Price ($)'])+2],
                  font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"))
fig.update_xaxes(title_text="Date")
fig.update_yaxes(title_text="Price (USD)")

# Save Figure
fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/26_202312252244.png")