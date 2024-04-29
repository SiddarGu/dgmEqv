
import plotly.graph_objects as go

fig = go.Figure(data=[go.Funnel(
    textinfo="value",
    y=['Proposal Submission','Conceptualization', 'Feasibility Study',
       'Project Planning', 'Implementation', 'Operation'],
    x=[1000, 800, 600, 400, 200, 100], 
    textposition="inside", 
    opacity=0.9, 
    marker_color='darkblue')])

fig.update_layout(
    title="Government Project Development in 2020",
    font=dict(
        family="Calibri",
        size=12,
        color="black"
    ),
    width=750,
    height=500,
    legend_orientation="h",
    paper_bgcolor="LightSteelBlue",
    plot_bgcolor="white"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/16.png")