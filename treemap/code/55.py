import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
raw_data = """Charity Sector,Donation Allocation (%)
Health Services,25
Education Programs,20
Environment and Wildlife,15
Arts and Culture,10
International Aid,10
Research and Development,10
Homelessness and Housing,5
Disaster Relief,5"""

# Split the data into lines
lines = raw_data.split('\n')

# Extract the data_labels from the first line
data_labels = lines[0].split(',')

# Initialize data and line_labels
data = []
line_labels = []

# Extract the numerical data and line labels from the rest of the lines
for line in lines[1:]:
    parts = line.split(',')
    line_labels.append(parts[0])
    data.append(float(parts[1]))

# Create a dataframe for the treemap
import pandas as pd
df = pd.DataFrame({
    data_labels[0]: line_labels, 
    data_labels[1]: data
})

# Create a treemap
fig = px.treemap(df, path=[data_labels[0]], values=data_labels[1],
                 title='Allocation of Donations Among Charity Sectors')

# Customize the treemap appearance
fig.update_traces(textinfo="label+value", textfont_size=20)

# Create the path if it doesn't exist
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
os.makedirs(save_path, exist_ok=True)

# Save the figure
fig.write_image(f"{save_path}/55.png")

# Clear the current image state since plotly doesn't maintain state
# No code necessary to clear state for plotly
