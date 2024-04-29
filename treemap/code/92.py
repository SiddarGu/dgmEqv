import plotly.express as px
import plotly.graph_objects as go
import os

# Transform the given data into three variables: data_labels, data, line_labels.

# Given data in a pseudo-CSV format.
raw_data = """
Internet Activity,Usage Share (%)
Social Media,25
Online Shopping,18
Streaming Services,17
Gaming,16
Online News,9
Cloud Services,8
Remote Work,4
E-Learning,3
"""

# Split the data into lines and then into entries
lines = raw_data.strip().split("\n")
data_labels = lines[0].split(",")[1:]
line_labels = [line.split(",")[0] for line in lines[1:]]
data = [float(line.split(",")[1]) for line in lines[1:]]

# Combine the data into a format suitable for plotly treemap
treemap_data = {
    'labels': line_labels,
    'values': data
}

# Create the treemap
fig = px.treemap(
    treemap_data,
    path=[px.Constant('Internet Activities'), 'labels'],
    values='values',
    title='Online Usage Distribution Across Internet Activities in 2023'
)

# Customize the layout to ensure all characters in labels show and are not overlapped
fig.update_traces(textinfo="label+percent entry", textfont_size=15)
fig.update_layout(
    uniformtext=dict(minsize=10, mode='hide'), 
    margin=dict(t=50, l=25, r=25, b=25)
)

# Create the directories for the output if not exist
output_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(output_dir, exist_ok=True)

# Save the figure
fig.write_image(f"{output_dir}/1114.png")

# If you were using matplotlib we would clear the figure here using plt.clf()
# But with plotly, we don't need to clear the current image state.
