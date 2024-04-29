import pandas as pd
import plotly.graph_objects as go

# Define the data
data = {
    "Date": [
        "2019-07-01",
        "2019-07-08",
        "2019-07-15",
        "2019-07-22",
        "2019-07-29",
        "2019-08-05",
        "2019-08-12",
        "2019-08-19",
        "2019-08-26",
        "2019-09-02",
    ],
    "Open Price ($)": [
        65.2,
        70,
        75.6,
        80,
        86.7,
        89.5,
        93.2,
        97.2,
        102.2,
        106.2,
    ],
    "Close Price ($)": [
        69.3,
        74.6,
        79.5,
        85.9,
        89.3,
        92.7,
        96.8,
        101.9,
        105.7,
        110.9,
    ],
    "High Price ($)": [
        70.5,
        75.0,
        80.1,
        86.3,
        90.1,
        93.5,
        97.2,
        102.6,
        106.3,
        111.6,
    ],
    "Low Price ($)": [
        64.2,
        68.0,
        74.9,
        79.5,
        85.1,
        89.0,
        92.7,
        96.5,
        101.7,
        105.9,
    ],
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Create a candlestick chart using plotly
fig = go.Figure(data=go.Candlestick(x=df["Date"],
                                   open=df["Open Price ($)"],
                                   high=df["High Price ($)"],
                                   low=df["Low Price ($)"],
                                   close=df["Close Price ($)"]))

# Update figure layout
fig.update_layout(
    title="Monthly Stock Performance in the Healthcare Industry",
    width=800,
    height=600,
    margin=dict(l=50, r=50, t=50, b=50),
    yaxis_range=[min(df["Low Price ($)"]) - 5, max(df["High Price ($)"]) + 5],
    xaxis_rangeslider_visible=False,
)

# Save the figure as a PNG image
fig.write_image("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/157_202312302255.png")