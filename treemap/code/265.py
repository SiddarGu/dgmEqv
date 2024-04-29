import plotly.express as px
import plotly.graph_objects as go
import os

# Data Preparation
data_labels = ['Logistics Volume (%)']
line_labels = ['Road Freight', 'Ocean Shipping', 'Rail Transport', 'Air Freight', 'Pipeline', 'Intermodal']
data = [35, 25, 20, 10, 5, 5]

# Create a treemap
fig = px.treemap(
    names=line_labels,
    parents=[""] * len(data),
    values=data,
    title='Distribution of Logistics Volume by Transportation Type',
)

# Stylize the treemap
fig.update_traces(
    textinfo='label+value',
    textfont=dict(size=18),
    marker=dict(line=dict(width=1)),
)

# Save the figure as PNG
save_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/'
os.makedirs(save_dir, exist_ok=True)
fig.write_image(os.path.join(save_dir, "1045.png"))

# Clear the current figure state
fig.data = []
