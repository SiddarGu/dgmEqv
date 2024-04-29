import plotly.express as px
import os

# Given data split into different variables
data_labels = ['Workforce Percent (%)']
line_labels = ['Administration', 'Sales', 'Marketing', 'Human Resources', 'Finance', 'IT', 'Customer Support', 'Research and Development']
data = [18, 22, 15, 10, 10, 10, 8, 7]

# Convert the data into a format suitable for a treemap
df_treemap = {
    'department': line_labels,
    'workforce_percent': data
}

# Create the treemap figure with plotly
fig = px.treemap(df_treemap, path=['department'], values='workforce_percent', title='Workforce Distribution Across Departments in Human Resources Management')

# Update layout if necessary
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
fig.update_traces(textinfo="label+value", textfont_size=20)

# Create the absolute save path, if path does not exist create the required directories
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/7.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
fig.write_image(save_path)

# Clear the figure to reset the state (if using in an environment where persistent state is an issue)
fig.data = []
