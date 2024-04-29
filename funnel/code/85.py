
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y=['Prospecting','Qualification','Needs Analysis','Solution Proposal','Closing'],
    x=[20000,15000,10000,5000,3000],
    textposition="inside",
    textinfo="value+percent initial",
    opacity=0.8,
    marker=dict(
        color='#000000'
    ),
)])

fig.update_layout(title_text="Investment Opportunities in Business and Finance in 2021",
                  font=dict(family="Calibri", size=18, color="#000000"),
    width=800,
    height=600
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/44.png")