
import plotly.graph_objects as go

fig = go.Figure(go.Funnel(
    y = ["Initial Investment", "Process Development", "Investment Expansion", "Loan Acquisition", "Loan Repayment"],
    x = [100, 88.8, 66.6, 46.2, 22.8],
    textinfo = "value+percent initial",
    marker = {"color": ['#ffd633', '#fec615', '#f9b700', '#f69e00', '#f48500']},
    textposition = "inside",
    opacity = 0.8
))

fig.update_layout(
    title={"text": "Financial Growth of Business in 2021"},
    font={"family": "Arial"},
    width=600,
    height=800,
    showlegend=False
)

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-49-51_simulation_num200/png/44.png")