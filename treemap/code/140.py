import plotly.express as px
import plotly.graph_objects as go
import os

# Given data
data_labels = ['Policy Spending (%)']
line_labels = ['Healthcare', 'Education', 'Defense', 'Social Security', 'Infrastructure', 'Energy', 'Science & Research', 'Environment', 'Agriculture']
data = [25, 20, 15, 15, 10, 5, 5, 3, 2]

# Combining the data into a single dataset suitable for the treemap
categories = {
    'Category': [],
    'Policy Spending (%)': []
}

# Populate categories dictionary
for label, value in zip(line_labels, data):
    categories['Category'].append(label)
    categories['Policy Spending (%)'].append(value)

# Create a DataFrame
df = pd.DataFrame(categories)

# Create a treemap
fig = px.treemap(df, path=['Category'], values='Policy Spending (%)',
                 title='Allocation of Government Spending on Public Policy Categories', 
                 color='Policy Spending (%)', 
                 color_continuous_scale='RdYlGn')

# Update layout to ensure a clear and intuitive visualization
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25), 
                  coloraxis_colorbar=dict(title="Spending %"))

# Save the figure
save_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(save_dir, exist_ok=True)
fig.write_image(f"{save_dir}/1107.png")

# Clear current image state (not needed in Plotly)
# For this Python environment, the plotly figure does not maintain state
# that needs to be explicitly cleared after saving.

# In case of matplotlib, fig.clear() or plt.close(fig) could be used.
