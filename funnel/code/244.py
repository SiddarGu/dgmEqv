
import plotly.graph_objects as go
import plotly.io as pio

# data
stage = ["Education", "Awareness", "Participation", "Institutionalization", "Change", "Sustainability"]
number = [1000, 800, 600, 400, 200, 100]

# create figure
fig = go.Figure()
fig.add_trace(go.Funnel(
    name="Environmental Sustainability",
    y=stage, 
    x=number,
    textinfo="value+percent initial",
    textposition="inside",
    textfont_color="white",
    texttemplate="%{x}",
    hovertemplate="%{y}: %{x}",
    marker={
        "color": ["#3eb54f","#9d8e75","#da9a6a","#da6a6a","#b14f4f","#964f4f"],
        "line": {
            "color": "white",
            "width": 2
        }
    }
))

# set figure layout
fig.update_layout(
    title="Environmental Sustainability - Progress Report in 2025",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="#7f7f7f"
    ),
    margin=dict(
        l=50,
        r=50,
        t=50,
        b=50
    ),
    paper_bgcolor="white",
    plot_bgcolor="white",
    showlegend=False,
    dragmode=False
)

# save figure
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/36.png", scale=4, width=1000, height=700, format="png")