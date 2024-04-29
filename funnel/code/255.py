
import plotly.graph_objects as go

fig = go.Figure(data=[go.Funnel(
    y = ["Awareness","Exploration","Engagement","Subscription","Adoption","Retention"],
    x = [1000000,800000,600000,400000,200000,100000],
    textinfo = "value+percent initial",
    textposition = "outside",
    opacity = 0.8,
    marker = {"color": ["#2ca02c", "#d62728", "#ff7f0e", "#2a7a2a", "#d62728", "#ff7f0e"]})])

fig.update_layout(title_text="User Growth in Technology and Internet in 2020",
                  font=dict(size=12),
                  legend=dict(x=0.85, y=1),
                  width=800,
                  height=600,
                  margin={"l":50,"r":50,"t":50,"b":50},
                  paper_bgcolor="white",
                  plot_bgcolor="white")

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/50.png")