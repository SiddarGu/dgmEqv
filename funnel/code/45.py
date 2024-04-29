
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Funnel(
    name="Legal Proceedings in 2033",
    y = ["Initial Inquiry", "Research & Analysis", "Initial Drafting", "Review & Refinement", "Final Drafting", "Filing & Execution"],
    x = [100, 85, 65, 45, 30, 15],
    textinfo="value+percent initial",
    textposition="inside",
    opacity=0.65
))

fig.update_layout(
    title="Legal Proceedings in 2033",
    font=dict(
        size=18,
    ),
    legend=dict(
        x=1,
        y=0.5
    ),
    paper_bgcolor="LightSteelBlue",
    width=900,
    height=600,
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-45-10_simulation_num50/png/11.png")