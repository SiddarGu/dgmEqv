
import plotly.graph_objects as go
import plotly.io as pio

# Set the title
title = 'Student Enrollment in Social Sciences and Humanities in 2020'

# Set the data
data = [
    dict(
        type='funnel',
        x=[1000, 800, 640, 512, 410],
        y=['Pre-enrollment', 'Inquiry', 'Application', 'Acceptance', 'Enrollment'],
        textinfo='value+percent initial',
        marker_color='royalblue',
        showlegend=False
    )
]

# Set the figure
fig = go.Figure(data=data)

# Set the layout
fig.update_layout(
    title=title,
    margin=dict(l=50, r=50, t=50, b=50),
    plot_bgcolor='white',
    paper_bgcolor='white',
    xaxis_title='Number of Students',
    yaxis_title='Stage',
    font=dict(
        family='Courier New, monospace',
        size=14,
        color='#000000'
    ),
    showlegend=True,
    legend=dict(
        x=1.02,
        y=1
    ),
)

# Save image
fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/37.png', width=1000, height=800, scale=2)