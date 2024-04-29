import os
import plotly.express as px
import plotly.graph_objects as go

# Provided data as a string
data_str = """Healthcare Aspect,Expenditure (%)
Hospital Care,40
Prescription Drugs,20
Physician Services,15
Dental Services,10
Nursing Home Care,7
Medical Research,5
Preventive Care,3"""

# Parsing the data into a list of lines
data_lines = data_str.split('\n')

# Parsing the header for the column labels
data_labels = data_lines[0].split(',')[1:]

# Parsing the row labels and data
line_labels = []
data_values = []
for line in data_lines[1:]:
    items = line.split(',')
    line_labels.append(items[0])
    data_values.append(float(items[1]))  # Convert string percentage to float

# Combining data for treemap plotting
data = {
    'labels': line_labels,
    'parents': [''] * len(line_labels),
    'values': data_values
}

# Create the treemap
fig = px.treemap(data, path=[px.Constant('Healthcare Expenditure'), 'labels'], values='values',
                 title='Percentage of Healthcare Expenditure by Services in 2023')

# Adjust the figure layout if necessary
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Before saving the figure, ensure the output directory exists
output_dir = "/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, '280.png')

# Save the figure
fig.write_image(output_path)

# Clear the current image state if needed (not applicable in this context, as Plotly manages its state internally)
