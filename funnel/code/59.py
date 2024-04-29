
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Initial Filing", "Pre-Trial Procedures", "Trial", "Appeal", "Final Ruling"],
    x = [100, 88.8, 66.6, 46.2, 22.8],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont = dict(
        color = "black",
        size = 12
    ),
    opacity = 0.75,
    marker = dict(
        color = ["#00A2FF","#00D8FF","#00FFFF","#90FF00","#FFD600"],
        line = dict(
            color = "white",
            width =  2
        )
    )
))
fig.update_layout(title_text="Legal Proceedings in Law and Legal Affairs in 2020",
                  font=dict(
                      family="Calibri, monospace",
                      size=14,
                      color="black"
                  ),
                  width=800,
                  height=800,
                  showlegend=False,
                  hovermode="x unified"
                  )
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-05-01_simulation_num100/png/79.png")