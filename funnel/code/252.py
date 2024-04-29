
import plotly.graph_objects as go
import plotly.io as pio

data=[go.Funnel(
        y=['Initial Inquiry','Feasibility Study','Project Planning','Implementation','Operation'],
        x=[7000,6300,5040,3360,1680],
        textinfo='value+percent initial',
        marker_color='#2ecc71',
        opacity=0.7,
        textposition='outside'
)]

fig = go.Figure(data=data)

fig.update_layout(
    title={
        'text':"Investment Opportunities in Business and Finance in 2020",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font={'family': 'Helvetica', 'size': 16, 'color': '#7f7f7f'},
    paper_bgcolor='#F2F2F2',
    plot_bgcolor='#F2F2F2',
    legend={'x':0.5,'y':0.1},
    width=1200,
    height=800,
    margin=dict(l=100,r=100,b=100,t=100,pad=4),
    showlegend=True)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/49.png")