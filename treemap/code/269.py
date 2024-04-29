import plotly.express as px
import os

# Create data based on the data provided
data_labels = ['Operations', 'Sales', 'Marketing', 'Human Resources',
               'Engineering', 'IT', 'Finance', 'Legal', 'Administration']
data = [25, 20, 15, 10, 10, 10, 5, 3, 2]
line_labels = ['Percentage of Workforce (%)']

# Create a DataFrame for the treemap
import pandas as pd
df = pd.DataFrame({'Department': data_labels, 'Percentage': data})

# Use plotly.express to create the treemap
fig = px.treemap(df, path=['Department'], values='Percentage',
                 title='Workforce Distribution Across Departments in a Corporate Environment',
                 color='Percentage', color_continuous_scale='Agsunset')

# Update the layout for better clarity and export quality
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Create necessary directory if it doesn't exist
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png'
os.makedirs(save_path, exist_ok=True)

# Save the figure
file_path = os.path.join(save_path, '1019.png')
fig.write_image(file_path)

# Display the figure if necessary (optional)
# fig.show()
