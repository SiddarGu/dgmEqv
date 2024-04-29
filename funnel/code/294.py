
import plotly.graph_objects as go
import plotly.io as pio

# data
Stage = ['Discovery', 'Exploration', 'Evaluation', 'Reflection', 'Application', 'Synthesis']
Number_of_Students = [500, 400, 300, 200, 100, 50]

# create figure
fig = go.Figure(data=[go.Funnel(
    y=Stage,
    x=Number_of_Students,
    textinfo="value+percent initial",
    orientation='h',
    marker_color='#6d8d77'
)])

# edit the layout
fig.update_layout(
    title={
        'text': "Student Learning Journey in Social Sciences and Humanities in 2020",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font=dict(
        family="Arial",
        size=15,
        color="#7f7f7f"
    ),
    xaxis=dict(
        title="Number of Students",
        titlefont=dict(
            size=14,
            color="#7f7f7f"
        )
    ),
    width=1000,
    height=800,
    showlegend=False,
    margin=dict(l=150),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)'
)

# save figure
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_14-14-53_simulation_num50/png/43.png")