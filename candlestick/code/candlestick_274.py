import plotly.graph_objects as go

data = [
    {
        'name': '2021-01-01',
        'open': 40,
        'close': 43,
        'high': 45,
        'low': 38
    },
    {
        'name': '2021-01-08',
        'open': 44,
        'close': 45,
        'high': 46,
        'low': 42
    },
    {
        'name': '2021-01-15',
        'open': 48,
        'close': 52,
        'high': 54,
        'low': 47
    },
    {
        'name': '2021-01-22',
        'open': 50,
        'close': 48,
        'high': 52,
        'low': 46
    },
    {
        'name': '2021-01-29',
        'open': 49,
        'close': 50,
        'high': 53,
        'low': 48
    },
    {
        'name': '2021-02-05',
        'open': 53,
        'close': 57,
        'high': 59,
        'low': 52
    },
    {
        'name': '2021-02-12',
        'open': 55,
        'close': 56,
        'high': 59,
        'low': 52
    },
    {
        'name': '2021-02-19',
        'open': 55.5,
        'close': 58,
        'high': 60,
        'low': 54
    },
    {
        'name': '2021-02-26',
        'open': 56,
        'close': 54,
        'high': 58,
        'low': 52
    },
    {
        'name': '2021-03-05',
        'open': 54,
        'close': 53,
        'high': 57,
        'low': 50
    },
]

# Create the candlestick chart
fig = go.Figure(data=[
    go.Candlestick(
        x=[d['name'] for d in data],
        open=[d['open'] for d in data],
        close=[d['close'] for d in data],
        high=[d['high'] for d in data],
        low=[d['low'] for d in data]
    )
])

# Set figure title
fig.update_layout(
    title='Weekly Stock Performance of a Sports and Entertainment Company',
    width=800,
    height=500,
    yaxis_range=[min([d['low'] for d in data]) - 5, max([d['high'] for d in data]) + 5],
    font_family='Arial, sans-serif'
)

# Save the chart image
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/171_202312302255.png')