
import plotly.graph_objects as go
import plotly.io as pio

fig = go.Figure(go.Funnel(
    y = ["Awareness", "Interest", "Consideration", "Intent", "Conversion", "Others"],
    x = [10000, 7000, 5000, 3000, 1000, 800],
    textinfo="value+percent initial",
    marker_line_color='#000000',
    marker_line_width=1,
    marker_color=['#FFA500', '#FFA500', '#FFA500', '#FFA500', '#FFA500', '#FFA500'],
    textposition="inside",
    texttemplate="%{x:.2s}",
    hoverlabel=dict(bgcolor="white",
                    font_size=16,
                    font_family="Rockwell")
))

fig.update_layout(title_text="Customer Acquisition - Food and Beverage Industry in 2020",
                  font=dict(family="Courier New, monospace",
                            size=18,
                            color="#000000"),
                  width=900,
                  height=600,
                  yaxis=dict(title_text="Stage",
                             titlefont=dict(family="Arial, sans-serif",
                                            size=18,
                                            color="black")),
                  xaxis=dict(title_text="Number of Customers",
                             titlefont=dict(family="Arial, sans-serif",
                                            size=18,
                                            color="black")),
                  legend_title="<b>Stage</b>",
                  showlegend=True,
                  legend=dict(x=1, y=1),
                  margin=dict(l=100, r=10, t=50, b=80),
                  paper_bgcolor='#EFE8E1',
                  plot_bgcolor='#EFE8E1')

fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/149.png")