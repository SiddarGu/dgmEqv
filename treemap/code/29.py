import os
import plotly.express as px

# Given data string (replaced '/n' with '\n' for correct line breaks)
data_string = """Discipline,Research Funding (%)
Biology,18
Computer Science,17
Engineering,20
Physics,15
Chemistry,12
Medicine,10
Environmental Science,5
Astronomy,3"""

# Splitting the data into lines
lines = data_string.strip().split("\n")

# Extracting the data labels (first line of data string)
data_labels = lines[0].split(",")[1:]

# Extract line labels and data
line_labels = []
data = []
for line in lines[1:]:
    parts = line.split(",")
    line_labels.append(parts[0])
    data.append(float(parts[1]))

# Preparing data for treemap plotting
frame = {
    'labels': line_labels,
    'values': data
}

# Create the treemap figure
fig = px.treemap(frame, path=['labels'], values='values',
                 title='Percentage Distribution of Research Funding Across Science and Engineering Disciplines')

# Update layout for clarity and aesthetics
fig.update_traces(textinfo='label+percent entry',
                  marker=dict(line=dict(width=0)),
                  textfont_size=16)

# Configure style
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Treemap saving path
save_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(save_dir, exist_ok=True)
save_path = os.path.join(save_dir, "1127.png")

# Save the figure
fig.write_image(save_path, scale=2)

# Note: No need to clear the current image state or use tight_layout(), as Plotly manages this internally.
