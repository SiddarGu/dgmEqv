
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

data = {'Stage': ['Initial Inquiry', 'Feasibility Study', 'Project Planning', 'Implementation', 'Operation'],
        'Number of Visitors': [400, 360, 280, 220, 120]}

df = pd.DataFrame(data)
fig = go.Figure(go.Funnel(
    name="Engagement in Arts and Culture in 2021",
    y=df["Stage"],
    x=df["Number of Visitors"],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.65,
    marker_color="royalblue",
    marker={
        'line': {'width': 0.5, 'color': 'white'}
    }
))

fig.update_layout(title_text="Engagement in Arts and Culture in 2021",
                  font=dict(
                      family="Courier New, monospace",
                      size=14,
                      color="#7f7f7f"
                  ),
                  paper_bgcolor="LightSteelBlue")
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/53.png", scale=1, width=1200, height=800, validate=False)