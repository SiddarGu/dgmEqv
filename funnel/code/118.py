
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set Data
stage = ["Research and Development", "Prototype Testing", "Production", "Quality Control", "Shipping"]
values = [20000, 15000, 10000, 7000, 4000]

# Set Figure
fig = make_subplots(rows=1, cols=1, specs=[[{"type": "funnel"}]],
                    subplot_titles=["Manufacturing and Production Process in 2021"])

fig.add_trace(go.Funnel(name='Process',
                         y=stage, 
                         x=values,
                         textinfo='value+percent initial'),
              row=1, col=1)

#Set Layout
fig.update_layout(uniformtext_minsize=18, uniformtext_mode='hide',
                  title_text="Manufacturing and Production Process in 2021",
                  height=800,
                  width=800,
                  showlegend=True,
                  legend_title_text='Process'
                 )

# Save Figure
fig.write_image('/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/67.png', width=800, height=800)