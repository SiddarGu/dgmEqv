import plotly.express as px
import os

# Input data
csv_data = """
Education Level, Government Funding (%)
Primary Education, 25
Secondary Education, 20
Tertiary Education, 30
Vocational Training, 10
Education Technology, 5
Adult Education, 7
Special Needs Education, 3
"""

# Processing input data
lines = csv_data.strip().split("\n")
data_labels = lines[0].split(", ")
line_labels = [line.split(", ")[0] for line in lines[1:]]  # Extracting first column for labels
data = [float(line.split(", ")[1]) for line in lines[1:]]  # Extracting numerical data

# Create treemap
fig = px.treemap(
    names=line_labels,
    parents=[""] * len(line_labels),
    values=data,
    title="Government Funding Distribution Across Educational Levels"
)

# Customizing the treemap
fig.update_traces(textinfo="label+value", textfont_size=20, marker=dict(colors=px.colors.qualitative.Pastel))
fig.update_layout(margin=dict(l=10, r=10, t=30, b=10))

# Ensure the directory exists
output_directory = "/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png"
os.makedirs(output_directory, exist_ok=True)

# Save treemap
fig.write_image(f"{output_directory}/1034.png")

# Clear current image state (not necessary for plotly)
