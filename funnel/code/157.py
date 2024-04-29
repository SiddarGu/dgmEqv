
import plotly.graph_objects as go

fig=go.Figure(go.Funnel(
    y = ["Research and Analysis","Proposal Preparation","Feasibility Study","Implementation","Monitoring and Evaluation"],
    x = [1000,888,666,462,228],
    textinfo="value+percent initial",
    marker_line_color='darkslategray',
    marker={'color': 'slategray'},
    opacity=0.8,
    textfont_size=12,
    textposition="inside",
    textfont_color="black"
))
fig.update_layout(
    title={"text":"Sustainability Initiatives - Progress in 2021",
    "font": {"size": 20},
    "x": 0.5,
    "xanchor": "center"},
    font=dict(
        family="Arial, monospace",
        size=12,
        color="#7f7f7f"
    ),
    width=800,
    height=600,
    xaxis_title="Number of Initiatives",
    yaxis_title="Stage",
    legend_title="Percentage of Initiatives",
    legend=dict(
        x=1.05,
        y=1.0
    )
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/154.png")