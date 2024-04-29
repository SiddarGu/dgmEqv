
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Initial Exposure", "Interest", "Evaluation", "Decision Making", "Post-Purchase", "Retention"],
    x = [1000, 900, 800, 700, 600, 500],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker_color = '#FFA500',
    opacity = 0.7,
    connector = {"line":{"color":"rgb(63, 63, 63)"}}))

fig.update_layout(
    title = "Engagement Funnel of Social Media and Web Users in 2021",
    font = dict(family = "Courier New, monospace", size = 14, color = "#7f7f7f"),
    showlegend = False,
    annotations = [dict(
        x = 0.97,
        y = 0.001,
        xref = "paper",
        yref = "paper",
        text = "Source:<br>Social Media and Web Users",
        showarrow = False
    )],
    xaxis_title = "Number of Visitors",
    yaxis_title = "Stage",
    plot_bgcolor = '#F4F4F8',
    paper_bgcolor = '#F4F4F8',
    height = 700,
    width = 800,
    margin = {"t":30, "b":30, "l":20, "r":20},
    hovermode = "closest"
)

# Save the figure
fig.write_image("../png/30.png")