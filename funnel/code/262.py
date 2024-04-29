
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Research and Development", "Prototyping", "Testing", "Production", "Delivery"], 
    x = [1000, 850, 700, 500, 200], 
    textinfo = "value+percent initial", 
    textposition = "inside", 
    marker = dict(
        color = ["#A4A4A4", "#636363", "#454545", "#2A2A2A", "#101010"]
    )
))

fig.update_layout(
    title = {
        'text': "Science and Engineering Projects in 2021", 
        'y':0.95, 
        'x':0.5, 
        'xanchor': 'center', 
        'yanchor': 'top'}, 
    font=dict(
        family="Courier New, monospace", 
        size=16, 
        color="#7f7f7f"
    ), 
    showlegend=False, 
    plot_bgcolor='#F2F2F2', 
    paper_bgcolor='#F2F2F2',
    margin=dict(t=50, b=50, l=120, r=120),
    width=700,
    height=700,
    hovermode = 'closest',
    funnelmode = 'group'
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/64.png")