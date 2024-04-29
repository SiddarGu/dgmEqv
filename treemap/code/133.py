import plotly.express as px

# Data processing
data_labels = ["Percent Contribution (%)"]
line_labels = ["Banking", "Insurance", "Investment", "Real Estate", "Information Technology", "Retail", "Manufacturing"]
data = [25, 15, 20, 15, 10, 10, 5]

# Creating a treemap
fig = px.treemap(
    names=line_labels, 
    parents=[""]*len(data),
    values=data,
    title='Percent Contribution to the Economy by Financial Sector'
)

# Adding fancy customizations
fig.update_traces(
    textinfo="label+value+percent root",
    textfont_size=15,
    hoverinfo='label+value+percent root',
    marker=dict(colors=px.colors.qualitative.Pastel, line=dict(width=2))
)

# Save the figure
fig.write_image("/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/133.png")

# This clears the figure
fig.data = []
