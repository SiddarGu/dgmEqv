
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure()

fig.add_trace(go.Funnel(
    y = ["Initial Screening", "Online Consultation", "In-Person Examination", "Diagnosis","Treatment", "Follow-up"],
    x = [1000, 900, 800, 700, 550, 300],
    textinfo = "value+percent initial",
    textposition = "outside",
    marker = dict(
        color = ["#a1c3d1", "#f28e2b", "#e15759", "#76b7b2", "#59a14f", "#edc948"]
    ),
    opacity = 0.7,
    connector = {"line":{"color":"#FFF",
                        "dash":"solid",
                        "width":2}
                 }
))

fig.update_layout(title="Healthcare and Health Services in 2020",
                  font=dict(family="Courier New, monospace",
                            size=14,
                            color="#7f7f7f"),
                  width=1000,
                  height=700,
                  legend_orientation="h",
                  paper_bgcolor="rgba(0,0,0,0)",
                  plot_bgcolor="rgba(0,0,0,0)",
                  showlegend=True,
                  margin=dict(l=30, r=30, t=50, b=50))

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/170.png")