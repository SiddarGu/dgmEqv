import plotly.express as px
import os

# Given string data that needs to be transformed into three variables: data_labels, data, line_labels
data_str = """Category,Usage (%)
Social Media,25
Online Shopping,20
Streaming Services,18
Cloud Computing,12
Online Gaming,10
Cybersecurity,8
Internet of Things,4
Online Education,3"""

# Split the data string into rows and then columns
data_rows = data_str.split('\n')
data_labels = data_rows[0].split(',')[1:]  # The category 'Usage (%)'
data = []
line_labels = []

# Process each line (excluding the header)
for line in data_rows[1:]:
    tokens = line.split(',')
    line_labels.append(tokens[0])  # The names of different categories
    data.append(float(tokens[1]))  # The corresponding usage percentages

# Construct the DataFrame
import pandas as pd
df = pd.DataFrame({
    'Category': line_labels,
    'Usage (%)': data
})

# Plot the Treemap using Plotly
fig = px.treemap(df, path=['Category'], values='Usage (%)', title='Internet Usage Distribution Across Technology Sectors')

# Save figure to absolute path
save_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
if not os.path.isdir(save_dir):
    os.makedirs(save_dir)
fig.write_image(os.path.join(save_dir, "93.png"))

# Clear the current image state
fig.data = []
