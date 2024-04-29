import plotly.express as px
import plotly.graph_objects as go
import os

# Given data as CSV-formatted string (where '/n' represents new lines)
data_csv = "Department,Budget Share (%)\nDefense,21\nHealthcare,18\nEducation,17\nSocial Security,15\nInfrastructure,10\nEnvironment,7\nScience and Technology,6\nAgriculture,4\nForeign Aid,2"

# Process the CSV data into the correct format
data_rows = data_csv.split('\n')
data_labels = data_rows[0].split(',')[1:]
line_labels = [row.split(',')[0] for row in data_rows[1:]]
data = [list(map(float, row.split(',')[1:])) for row in data_rows[1:]]

# Flatten the data to be used in the treemap
data_flat = [item for sublist in data for item in sublist]

# Create parent labels for the treemap (to display each sector/department)
parents = [''] * len(line_labels)

# Create a treemap using plotly
fig = px.treemap(
    names=line_labels,
    parents=parents,
    values=data_flat,
    title='Allocation of Government Budget Across Departments'
)

fig.update_traces(textinfo='label+percent parent')

# Set figure layout to adjust label text
fig.update_layout(
    uniformtext=dict(minsize=10)
)

# Set the figure size to prevent content from being displayed improperly
fig.update_layout(
    autosize=False,
    width=1200,
    height=800
)

# Define the output file path
output_dir = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png'
output_file = '1010.png'
os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists
output_path = os.path.join(output_dir, output_file)

# Save the figure at the specified path in PNG format
fig.write_image(output_path)

# Clear the current image state (not necessary for plotly)
# fig.clf() # This line would be used for matplotlib, but is not needed for plotly

print(f"Treemap saved at: {output_path}")
