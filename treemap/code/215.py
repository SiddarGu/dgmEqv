import plotly.express as px
import os

# Given data in text form, split it into separate lines
data_str = """Field,Research Funding (%)
Computer Science,22
Electrical Engineering,18
Mechanical Engineering,15
Civil Engineering,12
Chemical Engineering,10
Biomedical Engineering,8
Aerospace Engineering,7
Environmental Science,5
Materials Science,3"""

# Split data into rows and then columns
data_lines = data_str.strip().split('\n')
data_labels = data_lines[0].split(',')
line_labels = []
data = []

for line in data_lines[1:]:
    row_data = line.split(',')
    line_labels.append(row_data[0])
    data.append(float(row_data[1]))

df = {
    'values': data,
    'labels': line_labels
}

# Now we will use the labels and data to create a treemap and save it
fig = px.treemap(
    df,
    names=line_labels,
    values=data,
    path=['labels'],
    title='Allocation of Research Funding in Science and Engineering Fields'
)

# Customize the figure to make it fancy
fig.update_traces(
    textinfo="label+value",
    marker=dict(colors=px.colors.sequential.Rainbow, line=dict(color='#FFFFFF', width=2)),
    textfont=dict(size=18)
)
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25)
)

# Make directory if it doesn't exist
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png'
os.makedirs(save_path, exist_ok=True)
full_save_path = os.path.join(save_path, '215.png')

# Save the figure
fig.write_image(full_save_path)

# Clear the figure
fig.data = []
