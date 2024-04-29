
import plotly.graph_objects as go 
import plotly.io as pio 

fig = go.Figure(go.Funnel( 
    y = ["Registration","Account Activation","Validation","Verification","Usage","Post-Usage"], 
    x = [1000,800,600,400,200,180], 
    textinfo = "value+percent initial", 
    textposition = "inside", 
    marker_color = "royalblue", 
    opacity = 0.7, 
    connector = {"line":{"color":"royalblue","dash":"solid","width":1.5}}, 
    connector_visible = True, 
    showlegend = False)) 

fig.update_layout( 
    title = {"text":"Technology Adoption - Internet Users in 2020","x":0.5,"y":0.95}, 
    paper_bgcolor = "white", 
    plot_bgcolor = "white", 
    font = {"family":"Times New Roman"}, 
    height = 800, 
    width = 1000, 
    xaxis = {"visible":False}, 
    yaxis_title = "Stage", 
    yaxis = {"showgrid":True,"gridwidth":1.5,"gridcolor":"gainsboro","tickfont_size":10,"showticklabels":True}, 
    legend = {"x":0.77,"y":-0.3}
) 

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/190.png")