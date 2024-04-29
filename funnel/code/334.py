
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Interest","Research","Enquiries","Application","Acceptance","Commencement"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    textposition = "inside",
    opacity = 0.65,
    marker_color = 'darkblue',
    marker = dict(
        line = dict(
            color = '#000000',
            width = 2
        )
    )
))
fig.update_layout(
    title = {"text": "Education and Academics Admissions in 2021",
            "y":0.9,
            "x":0.5,
            "xanchor": "center",
            "yanchor": "top"},
    font = dict(
        family = "Courier New, monospace",
        size = 18,
        color = "#7f7f7f"
    ),
    paper_bgcolor = '#f3f3f3',
    plot_bgcolor = '#f3f3f3'
)
fig.write_image(r"/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-29_15-09-02_simulation_num50/png/22.png")