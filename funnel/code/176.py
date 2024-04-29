
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Information Gathering","Researching","Evaluation","Analyzing","Conclusion"],
    x = [1000,800,600,400,200],
    textinfo = "value+percent initial",
    marker = {"color": ["#FFC400", "#FFA300","#FF8200","#FF6100","#FF4000"],
             "line": {"width": [0, 0, 0, 0, 0],
                      "color": ["#FFC400", "#FFA300","#FF8200","#FF6100","#FF4000"]}},
    opacity = 0.8,
    connector = {"line": {"color": "#FFF",
                         "dash": "solid",
                         "width": 3}},
))

fig.update_layout(
    title = "Academic Journey - Social Sciences and Humanities in 2020",
    showlegend = True,
    width = 800,
    height = 1000,
    xaxis_title_text = "Number of Students",
    yaxis_title_text = "Stage",
    font = {"family": "Calibri", "size": 15},
    template = "plotly_white",
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/104.png")