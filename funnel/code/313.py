
import plotly.graph_objects as go 
fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [1000, 888, 666, 462, 228], 
    textinfo = "value+percent initial", 
    textposition = "inside",
    marker = {"line": {"width": 3, "color": "rgb(128,0,128)"}}))

fig.update_layout(
    title = {
        'text': "Real Estate Development in 2021", 
        'y':0.9, 
        'x':0.5, 
        'xanchor': 'center', 
        'yanchor': 'top'},
    font = dict(family="Courier New, monospace", size=18, color="#7f7f7f"),
    width=800, 
    height=600,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(t=130, b=20, l=50, r=50),
    showlegend = False,
    xaxis=dict(showgrid=True, gridwidth=1, gridcolor='LightPink', zeroline=True, showline=True, linewidth=2, linecolor='LightPink'),
    yaxis=dict(showgrid=True, gridwidth=1, gridcolor='LightPink', zeroline=True, showline=True, linewidth=2, linecolor='LightPink')
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/3.png")