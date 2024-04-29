
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Funnel(
    y = ["Research", "Consideration", "Comparison", "Acquisition", "Retention", "Others"],
    x = [1000, 800, 600, 400, 200, 100],
    textinfo = "value+percent initial",
    marker_color='royalblue',
    textposition="inside",
    opacity=0.7))
fig.update_layout(title_text="Online User Engagement - Technology and the Internet in 2021",
                  font=dict(family="Courier New, monospace", size=18),
                  width=1000,
                  height=700,
                  legend=dict(x=1.1, y=1))
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/148.png")