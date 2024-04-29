
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(data=[go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [1000, 800, 600, 400, 200, 160],
    textinfo = "value+percent initial",
    textposition = "inside",
    textfont = dict(size=12, color="white"),
    marker = dict(
        color = ["#1d8cf8","#f2bc2b","#45c490","#e75d4b","#f7d154","#e06377"],
        line = dict(
            color = "#ffffff",
            width = 1
        )
    ),
    opacity = 0.9)])

fig.update_layout(title_text="Social Media and Web Engagement in 2021",
                  width=800,
                  height=600,
                  font=dict(family="Arial", size=12))

fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#f5f5f5')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#f5f5f5')

fig.update_layout(legend=dict(x=0.9, y=1.1))

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/72.png")
pio.write_image(fig, "/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/72.png")