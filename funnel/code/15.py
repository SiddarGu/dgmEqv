
import plotly.graph_objects as go 
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    name = "Healthcare Quality Improvement in 2020",
    y=["Screening","Diagnosis","Treatment","Follow-up","Outcome"],
    x=[1000,800,600,400,200],
    textinfo="value"
))
fig.update_layout(title="Healthcare Quality Improvement in 2020", showlegend=True, 
                  font=dict(family="Calibri, monospace", size=18, color="#7f7f7f"))
fig.update_yaxes(title_text="Stage")
fig.update_xaxes(title_text="Number of Patients")
fig.update_layout(margin=dict(l=30, r=30, t=30, b=30))
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/3.png")