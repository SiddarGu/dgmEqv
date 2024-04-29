
import plotly.graph_objects as go

values = [100, 80, 60, 40, 20, 10]
labels = ['Initial Inquiry', 'Exploration', 'Feasibility Study', 'Project Planning', 'Implementation', 'Operation']

fig = go.Figure(go.Funnel(
    y = labels,
    x = values,
    textinfo = "value+percent initial",
    textfont_size = 14,
    opacity = 0.7,
    marker_color = 'royalblue',
    marker_line_color = 'black',
    marker_line_width = 0.5,
    connector = dict(line_color="darkslategray", line_width=1.5)
))

fig.update_layout(
    title = 'Energy Project Development in 2021',
    plot_bgcolor = 'white',
    paper_bgcolor = 'white',
    font_family = 'Roboto',
    font_size = 16,
    width = 500,
    height = 500,
    legend = dict(orientation="h")
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/158.png")