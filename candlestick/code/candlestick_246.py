
import plotly.graph_objects as go
import pandas as pd

# Set data
data = {'Month':['2019-05','2019-06','2019-07','2019-08','2019-09','2019-10'],
        'Open Price ($)':[35,45,48,51,52,55],
        'Close Price ($)':[40,50,52,54,56,57],
        'High Price ($)':[43,51,54,56,59,60],
        'Low Price ($)':[30,43,46,48,49,52]}

# Create dataframe from data
df = pd.DataFrame(data)

# Create figure
fig = go.Figure(data=[go.Candlestick(x=df['Month'], open=df['Open Price ($)'], high=df['High Price ($)'], low=df['Low Price ($)'], close=df['Close Price ($)'])])

# Update figure layout
fig.update_layout(title='Agriculture and Food Production Price Trend - Monthly Overview',
                  xaxis_title="Month",
                  yaxis_title="Price ($)",
                  yaxis_range=[min(df['Low Price ($)']),max(df['High Price ($)'])],
                  width=800,
                  height=600,
                  font=dict(family='Courier New, monospace', size=12, color='#7f7f7f'))

# Save figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/21_202312270043.png')