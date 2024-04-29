
import plotly.graph_objects as go 
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [10000, 8000, 6000, 4000, 2000, 1600],
    textinfo = "value+percent initial",
    textposition = "inside",
    marker_opacity=0.5,
    marker = {"color": ["#0041C2", "#00A1E4", "#3F92D2", "#7FC7E2", "#B6E0E6", "#DCE7ED"]},
    opacity=0.7,
    textfont_size = 10))

fig.update_layout(
    title_text = "Online Engagement - Technology and the Internet in 2020",
    showlegend=False,
    autosize=False,
    width=600,
    height=400,
    plot_bgcolor='rgba(0,0,0,0)'
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/21.png")