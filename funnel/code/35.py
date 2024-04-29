
import plotly.graph_objects as go
labels = ['Recruiting', 'Screening', 'Interview', 'Selection', 'Hiring']
values = [1000, 800, 600, 400, 200]
fig = go.Figure(go.Funnel(
    y = labels,
    x = values,
    textinfo = "value+percent initial",
    orientation = "h",
))
fig.update_layout(title={'text':'Employee Acquisition in Human Resources and Employee Management in 2021',
                         'y':0.90,'x':0.5,
                         'xanchor': 'center', 'yanchor': 'top'},
    font=dict(
        family="Courier New, monospace",
        size=10,
        color="#7f7f7f"
    ),
                  legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
fig.write_image('../png/35.png', width=800, height=400, scale=2)