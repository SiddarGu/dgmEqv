import plotly.express as px
import os

# Given data
data_labels = ['Higher Education', 'Secondary Education', 'Primary Education', 
               'Early Childhood Education', 'Special Education', 'Adult Education']
data = [35, 25, 20, 10, 5, 5]
line_labels = ['Public Spending (%)']

# Prepare the DataFrame for Plotly
df = {'Labels': data_labels, 'Spending': data}

# Plot using Plotly
fig = px.treemap(df, path=['Labels'], values='Spending', 
                 title='Allocation of Public Spending Across Educational Levels')

fig.update_traces(textinfo='label+percent entry')

# To ensure that text labels are clear and non-overlapping, adjust the text font size if needed
fig.update_layout(uniformtext=dict(minsize=10))

# Save the figure to the specified path
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/209.png"

# Create directory if it doesn't exist
os.makedirs(os.path.dirname(save_path), exist_ok=True)

fig.write_image(save_path)

# Clear the current image state if using plotly no need to explicitly clear the current image state
