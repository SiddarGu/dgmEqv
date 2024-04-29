
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    name="Energy and Utilities Projects in 2021",
    y=["Initial Research", "Feasibility", "Project Planning", "Execution", "Operation"],
    x=[100, 80, 60, 40, 20],
    textinfo="value+percent initial"))

fig.update_layout(title_text="Energy and Utilities Projects in 2021", font=dict(size=18))
fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
fig.update_layout(legend_orientation="h")
fig.update_traces(textposition="inside")
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightPink')
fig.update_layout(width=800, height=600, autosize=False, template="plotly_white")

# save the figure
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/192.png")