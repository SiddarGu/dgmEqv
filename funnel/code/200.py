
import plotly.graph_objects as go 
import plotly.io as pio

data = [
    dict(type='funnel', 
         y=['Awareness','Consideration','Interest','Intent','Purchase','Retention'],
         x=[9000,7600,6480,5424,4539,3791],
         textinfo="value+percent initial", 
         textposition="inside", 
         marker=dict(color='#1890FF', line=dict(color='#A6A6A6', width=2))
    )
]

fig = go.Figure(data) 
fig.update_layout(
    title='Shopping Funnel in Retail and E-commerce in 2021',
    font=dict(family='Courier New, monospace', size=18, color='#7f7f7f'),
    plot_bgcolor='white',
    showlegend=True,
    legend=dict(x=0, y=1.0, bgcolor='rgba(255, 255, 255, 0)', bordercolor='rgba(255, 255, 255, 0)'),
    margin=dict(l=100, r=50, t=50, b=50),
    hovermode='closest',
    paper_bgcolor='white',
    height=500,
    width=800,
    autosize=False
)
fig.write_image(r'../png/41.png')
pio.write_image(fig, r'../png/41.png')