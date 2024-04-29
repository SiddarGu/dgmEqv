import plotly.express as px
import plotly.graph_objects as go
import os

# Define the data
data = [
    ["Banking", 22],
    ["Investment", 18],
    ["Insurance", 15],
    ["Real Estate", 13],
    ["Technology", 12],
    ["Consumer Goods", 8],
    ["Health Care", 7],
    ["Energy", 5]
]

# Split the data into separate variables
data_labels = ["Market Share (%)"]
line_labels = [row[0] for row in data]
values = [row[1] for row in data]

# Plot the treemap
fig = px.treemap(
    names=line_labels,
    parents=[""] * len(data),
    values=values,
    title="Market Share Distribution Across Key Financial Sectors"
)

# Customize treemap
fig.update_traces(textinfo='label+percent entry')

# Make sure the labels are clear and not overlapping
fig.update_layout(uniformtext=dict(minsize=10))

# Save the figure to the specific path
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/118.png"
if not os.path.exists(os.path.dirname(save_path)):
    os.makedirs(os.path.dirname(save_path))

fig.write_image(save_path)

# Clear the figure (This is useful when using matplotlib but here in plotly it's not required)
# However, for the sake of the instruction given I'm writing it here. Plotly does not maintain state like matplotlib.
fig = None
