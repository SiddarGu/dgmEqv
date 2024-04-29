
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

data = [go.Funnel(
    y=["Searching", "Viewing", "Making Offer", "Negotiations", "Contract", "Closing"],
    x=[20000, 15000, 10000, 7000, 3000, 1000],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.65,
    marker=dict(
        color=['#a3a375', '#dcd6f7', '#efda47', '#786fa6', '#caa4e2', '#d9d8e0']
    )
)]
fig = go.Figure(data=data)
# fig = make_subplots(
#     rows=1, cols=2,
#     specs=[
#         [{"type": "funnel"}, {"type": "funnel"}]
#     ],
#     subplot_titles=[
#         # "Style 1",
#         # "Style 2"
#     ]
# )

# fig.add_trace(data[0], row=1, col=1)
# fig.add_trace(data[0], row=1, col=2)

fig.update_layout(
    showlegend=False,
    title = {
        'text': "Home Buying Process in the Real Estate Market in 2020",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    font=dict(family='Courier New, monospace', size=18, color='#7f7f7f'),
    margin=dict(l=20, r=20, t=50, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    width=1300,
    height=650,
    funnelmode='group',
    funnelgap=0.3,
    funnelgroupgap=0.1
)

fig.write_image("../png/29.png")