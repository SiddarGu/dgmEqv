import plotly.express as px
import os

# Process given data
data_str = """Government Department,Policy Spending (%)
Health and Human Services,25
Education,20
Defense,18
Welfare Programs,12
Transportation,9
Environment,7
Energy,5
Agriculture,4"""

# Splitting the data into lines and then into labels and values
lines = data_str.strip().split('\n')
data_labels = lines[0].split(',')[1:]
line_labels = []
data_values = []

for line in lines[1:]:
    parts = line.split(',')
    line_labels.append(parts[0])
    data_values.append(float(parts[1]))

data_labels = ["Policy Spending (%)"]
data = data_values

# Prepare the values and labels for the treemap
values = data
labels = line_labels

# Create the treemap

frame = {
    'labels': line_labels,
    'values': data
}

# frame, , values='values',

fig = px.treemap(
    frame,
    names=labels,
    values=values,
    path=['labels'],
    title='Allocation of Government Spending Across Departments'
)

# Customize the layout for better readability
fig.update_layout(
    treemapcolorway=["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A", "#19D3F3", "#FF6692", "#B6E880"],
    margin=dict(t=50, l=25, r=25, b=25)
)

# Verify if the directory exists, if not, create it
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/'
os.makedirs(save_path, exist_ok=True)
file_name = '122.png'

# Save the figure
fig.write_image(os.path.join(save_path, file_name))

# Clear the figure (not strictly necessary in a script that ends after plotting, but good practice)
fig = None
