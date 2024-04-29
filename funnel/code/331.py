
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Registration", "Attendance", "Retention", "Grades", "Graduation"],
    x = [1000, 800, 400, 200, 100],
    textinfo="value+percent initial",
    textposition="inside",
    marker_color='#7FC17B',
    marker = {"line": {"width": [1, 1, 1, 1, 1], "color": "#7FC17B"}},
    opacity=0.7,
    connector = {"line": {"color": "#7FC17B", "dash": "solid", "width": 1}}
))

fig.update_layout(
    title={
        'text': "Student Progress in Education and Academics in 2020",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    paper_bgcolor="LightSteelBlue",
    width=900,
    height=800,
    font=dict(
        family="Courier New, monospace",
        size=16,
        color="#7f7f7f"
    )
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/19.png")
#pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/19.png")