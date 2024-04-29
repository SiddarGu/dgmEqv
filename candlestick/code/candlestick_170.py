import plotly.graph_objects as go

data = [
    ["2020-01-01", 2000, 2100, 2500, 1950],
    ["2020-01-08", 2200, 2300, 2400, 2150],
    ["2020-01-15", 2200, 2350, 2500, 2180],
    ["2020-01-22", 2100, 2200, 2300, 2050],
    ["2020-01-29", 2150, 2250, 2400, 2100],
    ["2020-02-03", 2200, 2300, 2400, 2150],
    ["2020-02-10", 2250, 2350, 2500, 2200],
    ["2020-02-17", 2300, 2400, 2600, 2200]
]

dates = [row[0] for row in data]
open_donations = [row[1] for row in data]
close_donations = [row[2] for row in data]
peak_donations = [row[3] for row in data]
lowest_donations = [row[4] for row in data]

fig = go.Figure(data=[go.Candlestick(x=dates,
                                     open=open_donations,
                                     close=close_donations,
                                     high=peak_donations,
                                     low=lowest_donations)])

fig.update_layout(
    title="Weekly Donation Range in a Nonprofit Organization",
    xaxis_title="Date",
    yaxis_title="Donation Amount",
    width=800,
    height=600,
    yaxis_range=[min(lowest_donations) - 100, max(peak_donations) + 100]
)

fig.write_image(
    '/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/205_202312302255.png')