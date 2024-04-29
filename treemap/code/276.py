import plotly.express as px
import os

# Given data in CSV format
csv_data = """Legal Branch,Resource Allocation (%)
Judiciary,35
Law Enforcement,25
Legal Services,15
Prison System,10
Legislative Oversight,7
Regulatory Compliance,5
Legal Education,3
"""

# Parse data into a list of dictionaries
data = []
for line in csv_data.strip().split('\n')[1:]:
    parts = line.split(',')
    data.append({'Legal Branch': parts[0], 'Resource Allocation (%)': float(parts[1])})

# Convert data into a DataFrame for use in plotly
import pandas as pd
df = pd.DataFrame(data)

# Visualize the data using a treemap in plotly
fig = px.treemap(df, path=['Legal Branch'], values='Resource Allocation (%)', title='Allocation of Resources Among Legal Branches in 2023')

# Update the layout to make sure content is displayed without overlap
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Create directories if they don't exist
save_dir = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Save image
fig.write_image(f"{save_dir}/276.png")

# Clear the current image state to avoid accidental reuse
fig.data = []
