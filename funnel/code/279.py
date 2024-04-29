
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry", "Feasibility Study", "Project Planning", "Implementation", "Operation"],
    x = [1000, 888, 666, 462, 228],
    textinfo = "value+percent initial",
    marker = {"color": ["royalblue", "mediumseagreen", "gold", "crimson", "darkviolet"],
              "line": {"width": [2, 3, 4, 5, 6], "color": "white"}},
    opacity = 0.8,
    showlegend = True,
    textfont = {"size": 16}
))

fig.update_layout(
    title = {"text": "Sustainable Development by Organizations in 2021", 
             "font": {"size": 24, "family": "Calibri"}},
    margin = {"l": 150, "b": 100, "t": 100, "r": 50},
    height = 700,
    width = 1000,
    legend = {"x": 0.9, "y": 0.2},
    paper_bgcolor = "ghostwhite",
    plot_bgcolor = "ghostwhite"
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/111.png")