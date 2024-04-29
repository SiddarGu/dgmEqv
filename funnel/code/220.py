
import plotly.graph_objects as go
import pandas as pd

# Create DataFrame from the data
data = [['Initial Inquiry',5000],['Feasibility Study',4500],['Project Planning',4000],['Implementation',3000],['Follow-up',1500],['Others',1000]]
df = pd.DataFrame(data, columns = ['Stage', 'Number of Donors'])

# Create figure
fig = go.Figure(data=[go.Funnel(
    y = df['Stage'],
    x = df['Number of Donors'],
    textinfo = "value+percent initial",
    marker_color='royalblue',
    opacity=0.7,
    textposition="inside"
)])

# Set figure size
fig.update_layout(
    autosize=False,
    width=1000,
    height=800,
    title_text="Donor Engagement in Charity and Nonprofit Organizations in 2020"
)

# Set legend positioning
fig.update_layout(
    legend_orientation="h",
    legend=dict(x=0.5, y=-0.15)
)

# Save figure
fig.write_image("/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_19-18-21_simulation_num200/png/120.png")