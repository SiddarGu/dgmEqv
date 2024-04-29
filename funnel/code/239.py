

import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Discovery", "Exploration", "Evaluation", "Decision", "Retention"],
    x = [100000, 70000, 50000, 30000, 20000],
    textinfo="value+percent initial",
    marker_color='#a6cee3',
    textposition="inside",
    textfont_size=22,
    opacity=0.8,
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
))

fig.update_layout(
    title="Technology Adoption among Internet Users in 2021",
    font=dict(
        family="Courier New, monospace",
        size=14,
        color="#7f7f7f"
    )
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/21.png", width=800, height=800, scale=2)