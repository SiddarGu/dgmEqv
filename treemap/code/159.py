import plotly.express as px
import os

# Data transformation
raw_data = """
Hospital Services,30
Pharmaceuticals,22
Outpatient Care,18
Dental Services,12
Nursing Home Care,8
Preventive Care,5
Administration,3
Medical Equipment,2
"""

# Split the data into lines and then into labels and values
lines = raw_data.strip().split('\n')
data_labels = ['Health Sector', 'Expenditure (%)']
line_labels = [line.split(',')[0] for line in lines]
data_values = [float(line.split(',')[1]) for line in lines]

# Create a DataFrame for visualization
import pandas as pd
df = pd.DataFrame(list(zip(line_labels, data_values)), columns=data_labels)

# Create the treemap
fig = px.treemap(df, path=['Health Sector'], values='Expenditure (%)',
                 title='Percentage Distribution of Healthcare Expenditure Across Health Sectors',
                 color='Expenditure (%)', color_continuous_scale='RdBu')

# Update layout for better label visibility
fig.update_traces(textinfo='label+value', textfont_size=15)
fig.update_layout(uniformtext=dict(minsize=10, mode='hide'))

# Define the save path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/'
os.makedirs(save_path, exist_ok=True)  # This creates the directory if it does not exist

# Save the figure
fig.write_image(f"{save_path}159.png")

# Clear the figure (not strictly necessary in a standalone script, used here for completeness)
fig.data = []
