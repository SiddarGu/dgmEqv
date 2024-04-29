
import plotly.graph_objects as go
fig = go.Figure(data=[go.Funnel(
    y = ["Initial Consultation", "Diagnosis", "Treatment", "Follow-up", "Recovery", "Others"],
    x = [1000, 900, 700, 400, 200, 100],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.65,
    marker_color='#2A75BC',
    marker_line_width=3,
    marker_line_color='#2A75BC'
)])

fig.update_layout(
    title="Health Care Progress for Patients in 2020",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(
        color="rgba(255,255,255,1)"
    ),
    legend=dict(
        orientation="h",
        xanchor="center",
        yanchor="top",
        x=.5,
        y=-0.2
    )
)
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/162.png", width=1300, height=800, scale=2)