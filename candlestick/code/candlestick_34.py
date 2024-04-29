
import plotly.graph_objects as go
import pandas as pd
fig = go.Figure(data=[go.Candlestick(x=pd.date_range('2019-04-26', periods=7),
open=[350.2,372,360,375,380,383.6,387.3],
high=[379,384.5,376.3,390.9,396.2,392.7,393.4],
low=[340.8,350.3,353.4,364.1,374.8,378.9,372.7],
close=[368.4,368.9,369,385.2,391,388.4,381.2])])

fig.update_layout(title='Business and Finance Trend - Weekly Overview',
yaxis_range=[340,400],
width=1400,
height=700,
template="plotly_white")
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/15_202312270043.png')