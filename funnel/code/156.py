
import plotly.graph_objects as go
import plotly.io as pio

values = [1000, 888, 666, 462, 228]
phases = ['Initial Inquiry', 'Feasibility Study', 'Project Planning', 'Implementation', 'Operation']

fig = go.Figure(go.Funnel(
    y = phases, 
    x = values,
    textinfo = "value+percent initial",
    marker = {"color": ["#00BFFF", "#FFD700", "#FF8C00", "#FF4500", "#CD5C5C"]},
    opacity = 0.8
))

fig.update_layout(title_text="Business and Finance Growth in 2020",
                  font=dict(family="sans serif"),
                  width=1000,
                  height=600,
                  showlegend=True,
                  margin=dict(l=20, r=20, t=40, b=20)
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/151.png")