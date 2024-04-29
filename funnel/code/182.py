
import plotly.graph_objects as go

data = [
    {'stage': 'Research', 'num_workers': 50},
    {'stage': 'Design', 'num_workers': 40},
    {'stage': 'Production', 'num_workers': 30},
    {'stage': 'Quality Control', 'num_workers': 20},
    {'stage': 'Shipping', 'num_workers': 10}
]

fig = go.Figure(data=[go.Funnel(
    y=list(map(lambda x:x['stage'], data)),
    x=list(map(lambda x:x['num_workers'], data)),
    textposition="inside",
    textinfo="value+percent initial",
    opacity=0.9,
    marker_color='green')])

fig.update_layout(title_text='Manufacturing and Production Performance in 2021',
                  font={'family':'Times New Roman'},
                  legend_orientation="h",
                  width=800,
                  height=1000,
                  margin=dict(l=0, r=0, t=50, b=50),
                  paper_bgcolor="LightSteelBlue")

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/196.png")