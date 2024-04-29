
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [1000, 900, 800, 700, 600, 500],
    textinfo = "value+percent initial"))

fig.update_layout(
    title = {
        'text': "Environmental Sustainability - Volunteer Engagement in 2021",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    font = dict(
        family="Times New Roman",
        size=18,
        color="black"
    ),
    showlegend=True,
    legend=dict(
        yanchor="bottom",
        y=0.04,
        xanchor="left",
        x=0.95))

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/12.png", scale=2, width=1300, height=750)