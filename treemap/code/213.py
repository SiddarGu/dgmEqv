# Import necessary libraries
import plotly.express as px

# Given data
data = """
Legal Branch,Expenditure (%)
Judiciary,25
Law Enforcement,35
Correctional Facilities,15
Legal Services,10
Regulatory Agencies,7
Legal Education,5
Public Defense,3
"""

# Parsing the data into lists
split_data = data.strip().split("\n")
data_labels = split_data[0].split(",")[1:]
line_labels = [row.split(",")[0] for row in split_data[1:]]
values = [int(row.split(",")[1]) for row in split_data[1:]]

# Building hierarchical data structure
structure = {
    'labels': line_labels,
    'values': values,
    'parents': [""] * len(line_labels)
}

# Create the treemap using Plotly
fig = px.treemap(
    structure,
    names='labels',
    parents='parents',
    values='values',
    title='Budgetary Shares of Different Branches within Law and Legal Affairs'
)

# Update the layout
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
)

# Save the figure to the specified absolute path
fig.write_image("/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/213.png")
