
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Initial Inquiry","Feasibility Study","Project Planning","Implementation","Operation"],
    x = [100,90,80,60,40],
    textinfo = "value+percent initial",
    marker_line = {"width":[0.5,0.5,0.5,0.5,0.5],
                   "color":["#444","#444","#444","#444","#444"]},
    opacity = 0.9
))

fig.update_traces(textfont_size=18,
                  marker = {"line":{"width":[1.5,1.5,1.5,1.5,1.5],
                                   "color":["#444","#444","#444","#444","#444"]}},
                  hovertemplate = None)

fig.update_layout(title_text="Energy Sector Project Development in 2020",
                  font_size=18,
                  legend_orientation="h",
                  legend=dict(x=0.5,y=-0.15),
                  width=700,
                  height=700,
                  paper_bgcolor="white",
                  plot_bgcolor="white",
                  showlegend=True)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/1.png")