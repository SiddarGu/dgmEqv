
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Admissions", "Orientation", "Course Selection", "Study", "Assessment", "Graduate"],
    x = [1000, 900, 800, 700, 600, 500],
    textinfo = "value+percent initial",
    marker = {"color": ["#0099CC", "#003366", "#CCCC00", "#00FF00", "#9900CC", "#FF6600"]},
    textposition = "inside",
    textfont = {"size": 12},
    opacity = 0.7,
    hoverinfo = "text+x",
    hoverlabel = {"bgcolor": "white", "font": {"size": 14}}
))

fig.update_layout(
    title = {
        "text": "Student Engagement in Social Sciences and Humanities in 2020",
        "x": 0.5,
        "y": 0.95,
        "xanchor": "center",
        "yanchor": "top"
    },
    width = 800,
    height = 600,
    showlegend = True,
    legend = {"x": 0.8, "y": 0.5, "xanchor": "center", "yanchor": "middle"},
    paper_bgcolor = "white",
    plot_bgcolor = "white",
    xaxis_title = "Number of Students",
    yaxis = {"ticks": "outside", "ticklen": 3, "tickcolor": "black", "tickwidth": 1}
)
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/29.png")