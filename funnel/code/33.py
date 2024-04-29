
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

data = [go.Funnel(
    y=['Incoming Parts','Processing','Assembly','Finished Goods','Packaging','Shipping'],
    x=[1000,800,600,400,200,100],
    textinfo='value+percent initial')]

fig = go.Figure(data)
fig.update_layout(title_text='Manufacturing and Production in 2024',
                  font=dict(family='Courier New, monospace',
                            size=18,
                            color='#7f7f7f'),
                  margin={'l':50,'r':50,'b':50,'t':50})
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#EEEEEE', linewidth=2, linecolor='#444444')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#EEEEEE', linewidth=2, linecolor='#444444')
fig.update_layout(showlegend=False)
fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/38.png', width=1500, height=1000, scale=2)