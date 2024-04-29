import os
import plotly.express as px
import plotly.graph_objects as go

# Parse the given data.
raw_data = """
Healthcare Aspect, Expenditure (%)
Public Health Services,25
Hospital Care,35
Pharmaceuticals,15
Research & Development,10
Mental Health Services,5
Long-Term Care,5
Preventive Care,3
Administrative Costs,2
"""

# Process data into required format.
lines = raw_data.strip().split('\n')
data_labels = [lines[0].split(',')[0]]
line_labels = []
data = []

for line in lines[1:]:
    items = line.split(',')
    line_labels.append(items[0])
    data.append(float(items[1]))

# Create a treemap using plotly express.
fig = px.treemap(
    names=line_labels,
    values=data,
    parents=[""] * len(data),
    title="Allocation of Healthcare Expenditure by Services in 2023"
)

# Customize the treemap.
fig.update_traces(
    textinfo="label+percent parent",
    hoverinfo="label+value+percent parent",
    textfont=dict(size=18),
    marker=dict(line=dict(width=0)),
    tiling=dict(squarifyratio=1.5)  # Customized for aesthetic purposes.
)

# Ensure all text fits and is not overlapping.
fig.update_layout(
    uniformtext=dict(minsize=10, mode='hide')
)

# Save the figure.
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/216.png"

# Create the directory if it does not exist.
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure representation to the file in PNG format.
fig.write_image(save_path)

# Clear the current image state.
fig.for_each_trace(lambda t: go.FigureWidget().add_trace(t))
