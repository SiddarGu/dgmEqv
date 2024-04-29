import plotly.graph_objects as go

data = {'Date': ['2023-01-01', '2023-01-08', '2023-01-15', '2023-01-22', '2023-01-29', '2023-02-05', '2023-02-12', '2023-02-19', '2023-02-26'],
        'Open Price ($)':[120, 122, 125, 130, 132, 137, 140, 143, 149],
        'Close Price ($)':[119, 123, 128, 134, 135, 138, 142, 147, 153],
        'High Price ($)': [122, 125, 130, 137, 139, 140, 145, 150, 154],
        'Low Price ($)': [115, 119, 121, 128, 129, 134, 137, 139, 145]}

df = pd.DataFrame(data)

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open Price ($)'],
                high=df['High Price ($)'],
                low=df['Low Price ($)'],
                close=df['Close Price ($)'])])

fig.update_layout(
    title_text='Humanities and Social Science Books Sales Analysis',
    width=800,
    height=600,
    autosize=False,
    yaxis_range=[110, 160],
    showlegend=False,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=0
    ),
    paper_bgcolor='white',
    plot_bgcolor='white',
    )

fig.update_traces(
    decreasing_line_color='rgb(255,0,0)',
    increasing_line_color='rgb(0,128,0)',
    )

fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/77_202312302255.png')