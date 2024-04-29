
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(y=["Consultation","Diagnosis","Treatment","Follow-up","Recovery"],
                        x=[1000,900,800,700,600],
                        textinfo="value+percent initial"))
fig.update_layout(title_text="Patient Care Journey in Healthcare and Health Sector in 2021",
                  font=dict(family="sans-serif"),
                  showlegend=False,
                  margin=dict(l=0, r=0, t=80, b=0),
                  paper_bgcolor="LightSteelBlue",
                  plot_bgcolor="LightSteelBlue",
                  yaxis_title="Stage",
                  xaxis_title="Number of Patients",
                  width=800, 
                  height=500,
                  )

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/189.png")