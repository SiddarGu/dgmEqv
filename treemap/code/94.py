import plotly.express as px
import plotly.graph_objects as go
import os

# Parse the data
data = """
Judicial Branch,Case Load (%)
Supreme Court,5
Appellate Courts,15
District Courts,50
Bankruptcy Courts,10
Special Jurisdiction Courts,20
"""

# Split the data into lines and then separate labels from data
lines = data.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in lines[1:]]
case_loads = [int(line.split(',')[1]) for line in lines[1:]]

# Map the data into parents and ids for a treemap
parents = ['',] * len(line_labels)  # No parents since they are all top-level categories
ids = line_labels

# Create the data frame
data_frame = {'ids': ids, 'parents': parents, 'case_load': case_loads, 'labels': line_labels}

# Create the treemap
fig = px.treemap(
    data_frame,
    names='labels',
    parents='parents',
    values='case_load',
    title='Case Load Distribution Across U.S. Judicial Branches'
)

# Customize the treemap colors, if desired
fig.update_traces(
    hoverinfo='label+value+percent parent',
    textinfo='label+percent parent',
    marker=dict(colors=px.colors.qualitative.Pastel),
    textfont=dict(size=16)
)

# Define the save path
save_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/'
save_path = os.path.join(save_dir, '94.png')

# Create directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

# Save the figure
fig.write_image(save_path)

# Clear the figure after saving
fig.data = []
