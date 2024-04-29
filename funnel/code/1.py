
import plotly.graph_objects as go
import plotly.io as pio

# set data 
data = {
    'stage': ['Research and Development', 'Design and Engineering', 'Production', 'Quality Control', 'Delivery', 'Support'], 
    'Number of Products': [1000, 800, 600, 400, 200, 100]
}

# create a figure
fig = go.Figure()

# add trace
fig.add_trace(go.Funnel(
    y = data['stage'], 
    x = data['Number of Products'], 
    textinfo = "value+percent initial", 
    textposition="inside",
    marker_color='#2ecc71'
))

# update figure layout
fig.update_layout(
    title = {
        'text': "Manufacturing and Production - Product Output in 2023",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    font=dict(family='sans-serif'),
    showlegend = False,
    margin=dict(l=200),
    width=800,
    height=800,
    xaxis_title="Number of Products",
    yaxis_title="Stage",
)

# write image
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-26_05-57-56_simulation_num50/png/38.png")