
import plotly.graph_objects as go
import plotly.io as pio

data = [
  {"stage":"Advertising","Number of Attendees":1000},
  {"stage":"Ticket Sales","Number of Attendees":800},
  {"stage":"Attendance","Number of Attendees":600},
  {"stage":"Post-Event Reviews","Number of Attendees":400},
  {"stage":"Follow-up Surveys","Number of Attendees":200},
  {"stage":"Others","Number of Attendees":100}
]

labels = [d['stage'] for d in data]
values = [d['Number of Attendees'] for d in data]

fig = go.Figure(data=[go.Funnel(
    y=labels, x=values, textinfo="value+percent initial",
    opacity=0.5, marker=dict(
        color="mediumturquoise",
        line=dict(color="mediumturquoise", width=2)
    )
)])

fig.update_layout(
    title="Arts and Culture Festival Participation in 2021",
    font=dict(
        size=14,
        color="black"
    ),
    paper_bgcolor="white",
    plot_bgcolor="white",
    autosize=False,
    width=600,
    height=600,
    showlegend=False,
    margin=go.layout.Margin(
        l=100,
        r=100,
        b=100,
        t=100,
        pad=4
    ),
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/87.png")