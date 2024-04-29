
import plotly.graph_objects as go
import plotly.io as pio

stage = ["Initial Inquiry","Feasibility Study","Project Planning","Implementation","Operation"]
num_donors = [100,80,60,40,20]

fig = go.Figure(data=[go.Funnel(
    y=stage,
    x=num_donors,
    textinfo="value+percent initial",
    marker_color='#4572A7',
    marker=dict(line=dict(width=1, color='#333')),
    opacity=0.7,
    hoverinfo='text',
    textposition="inside",
    texttemplate="%{x:.0f} Donors"
)])

fig.update_layout(
    title="Increasing Donor Engagement in Charity and Nonprofit Organizations",
    showlegend=False,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(
        l=50,
        r=50,
        t=50,
        b=50
    ),
    font_size=12
)

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey')

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/146.png", width=900, height=500, scale=2)