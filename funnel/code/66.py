
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Inquiry", "Pre-Trial", "Trial", "Appeal", "Final Judgment", "Post-Judgment"],
    x = [1000,800,600,400,200,100],
    textinfo = 'value+percent initial',
    textposition = "inside",
    opacity = 0.65,
    marker_color = 'royalblue',
    ))

fig.update_layout(
    title = {"text": "Legal Disputes Resolution Process in Law and Legal Affairs in 2021",
             "font": {"size":20},
             "x": 0.5},
    font = {"family": "Times New Roman"},
    legend_title_text = 'Number of Cases',
    legend=dict(
        x=0.6,
        y=1.2,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    width = 800,
    height = 600,
    margin = {'l':0, 'b':0, 't':50, 'r':0},
    template = "plotly_white"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/86.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/86.png")