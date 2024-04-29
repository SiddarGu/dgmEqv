

import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y=[ "Recruitment", "Onboarding", "Training", "Performance Management","Rewards & Recognition"],
    x=[100, 88.8, 66.6, 46.2, 22.8],
    textinfo="value+percent initial",
    marker=dict(
        color='royalblue',
        line=dict(color='royalblue', width=2)
    )
)])

fig.update_layout(title={'text': 'Employee Management and Development in Human Resources in 2020',
                         'y':0.98,
                         'x':0.5,
                         'xanchor': 'center',
                         'yanchor': 'top'},
                   font=dict(
                         family="Courier New, monospace",
                         size=12,
                         color="#7f7f7f"
                         ),
                   legend=dict(
                         x=0.5,
                         y=1.1
                         ),
                   plot_bgcolor='white',
                   width=800,
                   height=800,
                   margin=dict(l=20, r=20, t=20, b=20),
                   paper_bgcolor='white',
                   hovermode='closest',
                   showlegend=False,
                   xaxis=dict(showgrid=True, zeroline=False),
                   yaxis=dict(showgrid=True, zeroline=False)
                   )

fig.write_image("../png/272.png")