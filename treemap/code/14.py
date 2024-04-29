import plotly.express as px
import os

# Data given
data_labels = ['University Budget Allocation (%)']
line_labels = ['Natural Sciences', 'Engineering and Technology', 'Medicine and Health', 'Social Sciences', 
               'Arts and Humanities', 'Business and Economics', 'Law', 'Education']
data = [22, 18, 17, 14, 12, 10, 4, 3]

# Create a DataFrame for Plotly
import pandas as pd
df = pd.DataFrame(list(zip(line_labels, data)), columns=['Subject Area', 'Budget Allocation'])

# Create treemap using Plotly Express
fig = px.treemap(df, path=['Subject Area'], values='Budget Allocation',
                 title='University Budget Allocation Across Various Academic Disciplines in 2023')

# Customize the layout
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Save the figure
save_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/'
save_path = os.path.join(save_dir, '14.png')

# Ensure the directory exists
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
fig.write_image(save_path)
