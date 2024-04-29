import plotly.express as px
import os

# Input data as a multiline string for easier parsing
raw_data = """
Medicine,22
Engineering,18
Computer Science,15
Physics,12
Biology,10
Economics,8
Sociology,5
Chemistry,5
Mathematics,3
Linguistics,2
"""

# Parse the raw data into line_labels and data
line_labels = []
data = []

for line in raw_data.strip().split('\n'):
    discipline, funding = line.split(',')
    line_labels.append(discipline)
    data.append(float(funding))

# Since there's only one column of data, data_labels will have just one element
data_labels = ["Research Funding Allocation (%)"]

# Setup Plotly treemap
fig = px.treemap(
    names=line_labels,
    parents=[""] * len(line_labels),
    values=data,
    title="Allocation of Research Funding Across Academic Disciplines",
)

# Make the image fancy as per requirement
fig.update_traces(textinfo="label+value", textfont_size=18)
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Define the output directory and create it if it doesn't exist
output_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(output_dir, exist_ok=True)

# Save the figure
file_path = os.path.join(output_dir, "241.png")
fig.write_image(file_path)

# Clear the current image state if using `matplotlib`, not necessary with Plotly
# plt.clf() or plt.close() would be used if matplotlib was being used.

# Output the saved image path
print(f"Image saved to {file_path}")
