
import plotly.graph_objects as go
import pandas as pd

# prepare data
data = [["2019-06-17", 100, 105, 110, 90],
        ["2019-06-24", 97, 104, 105, 93],
        ["2019-07-01", 98, 100, 103, 96],
        ["2019-07-08", 94, 95, 97, 90],
        ["2019-07-15", 90, 93, 96, 87],
        ["2019-07-22", 88, 90, 93, 85],
        ["2019-07-29", 85, 87, 90, 81]]
df = pd.DataFrame(data, columns=["Date", "Opening Price ($)", "Closing Price ($)", "High Price ($)", "Low Price ($)"])

# create figure
fig = go.Figure(data=[go.Candlestick(
    x=df["Date"],
    open=df["Opening Price ($)"],
    high=df["High Price ($)"],
    low=df["Low Price ($)"],
    close=df["Closing Price ($)"])])

# update figure
fig.update_layout(title_text="Financial Trends of Charity and Nonprofit Organizations",
                  yaxis_range=[80,110],
                  width=800,
                  height=300,
                  font=dict(family="sans-serif",
                            size=12))

# save figure
fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/19_202312270043.png")