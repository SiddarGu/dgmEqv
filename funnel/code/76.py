
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    name='Adoption of Technology and the Internet in 2021',
    y=['Research','Evaluation','Comparison','Purchase','Retention','Referrals'],
    x=[500000,400000,300000,200000,100000,80000],
    textinfo="value+percent initial",
    textfont_size=14,
    textposition="inside",
    marker_color='#2CA02C',
))

fig.update_layout(
    title="Adoption of Technology and the Internet in 2021",
    title_x=0.5,
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)

fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.update_layout(height=600, width=800, legend_orientation="h")
fig.write_image("../png/18.png")