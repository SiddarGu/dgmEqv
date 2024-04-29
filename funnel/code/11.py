
import plotly.graph_objects as go
fig = go.Figure(go.Funnel(
    y = ["Awareness","Interest","Consideration","Intent","Conversion"],
    x = [1000,750,500,250,100], 
    textinfo = "value",
    orientation = "h",
    textfont_size = 10,
    marker_color = "royalblue"))
fig.update_layout(
    title = "Visitor Conversion Rate - Tourism and Hospitality in 2021",
    paper_bgcolor = "white",
    plot_bgcolor = "white")
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_17-38-49_simulation_num50/png/8.png", width = 1000, height = 600)