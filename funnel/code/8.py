
import plotly.graph_objects as go

data = [
    go.Funnel(
        y=['Enrollment','Applicants','Application review','Interview','Admission'],
        x=[1000,800,400,200,100],
        textinfo='value',
        orientation='h',
        marker_color='royalblue'
    )
]

fig = go.Figure(data)

fig.update_layout(
    title = 'Admissions in Science and Engineering in 2021',
    font = dict(size=14),
    legend_orientation="h",
    width=800,
    height=600
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/25.png")