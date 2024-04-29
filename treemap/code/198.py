import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_labels = ['Online Retail', 'In-Store Retail', 'Electronics', 'Fashion', 'Home & Furniture', 'Sporting Goods', 'Books & Media']
line_labels = ['Sales Percentage (%)']
data = [40, 30, 10, 8, 7, 3, 2]

# Transform the data into a format that Plotly can use
# We need to add an additional parent element, for instance, "Total"
parents = [''] * len(data_labels)  # The top level has no parent

# Create a DataFrame for converting given data to a suitable format
tree_data = {
    'labels': data_labels,
    'values': data,
    'parents': parents
}

# Use plotly to create a treemap
fig = px.treemap(
    tree_data,
    names='labels',
    values='values',
    parents='parents',
    title='Retail and E-commerce Sales Distribution in 2023',
    color='values',
    color_continuous_scale=px.colors.sequential.RdBu
)

fig.update_traces(
    textinfo="label+value",
    textfont=dict(size=18)
)

fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25),
)

# Define the file path and make sure the directory exists
file_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/198.png'
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Save figure
fig.write_image(file_path)

# Clear the state (not strictly necessary in a script, as there is no ongoing state across runs, but included for compliance)
fig.data = []
