import plotly.express as px
import plotly.graph_objects as go
import os

# Given raw data
raw_data = """Category,Traffic Share (%)
Social Media,25
Search Engines,20
E-Commerce,15
Online Education,10
Streaming Services,10
Cloud Services,8
Cybersecurity,7
Internet of Things,5"""

# Transforming raw data into separate variables for plotting
rows = raw_data.split('\n')
data_labels = rows[0].split(',')[1:]  # Get the labels of each column except the first
line_labels = [row.split(',')[0] for row in rows[1:]]  # Get the labels of each row except the first
data = [float(row.split(',')[1]) for row in rows[1:]]  # Get the numerical array in the data

# Initialize an empty list to hold our processed data
formatted_data = []

# Populate the formatted_data list with dictionaries for plotly
for i in range(len(data)):
    formatted_data.append({
        'labels': line_labels[i],
        'parents': "",
        'values': data[i]
    })

# Creating a dataframe for Plotly
fig_data = {
    'labels': line_labels,
    'parents': [''] * len(data),
    'values': data
}

# Creating the treemap using plotly
fig = px.treemap(fig_data, path=['labels'], values='values', title='Web Traffic Distribution Across Internet Services')

# Customize layout
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25)
)

# Customize treemap appearance
fig.update_traces(textinfo="label+value", textfont_size=15)

# Define the save path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/188.png'
# Ensure the directory exists before saving
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save figure
fig.write_image(save_path)

# Clear the current image state
fig.data = []
