
import plotly.graph_objects as go
import plotly.io as pio

stage = ['Interest', 'Engagement', 'Participation','Interaction', 'Imitation', 'Innovation']
number_of_people = [10000, 8000, 6000, 4000, 2000, 1600]

fig = go.Figure(go.Funnel(
    y = stage,
    x = number_of_people,
    textinfo = "value+percent initial",
    marker_color = "royalblue",
    opacity = 0.8,
    orientation='h'
))

fig.update_traces(textposition='inside')
fig.update_layout(
    title = {
        'text': "Arts & Culture Engagement - A Funnel Analysis in 2020",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    template="plotly_dark",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    ),
    xaxis=dict(
        title="Number of People",
        gridcolor='#222222'
    ),
    margin=dict(
        l=200,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    width=800,
    height=800,
    showlegend=False
)

fig.write_image(r"/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/59.png")