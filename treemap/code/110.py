import os
import plotly.express as px

# Given data
data_labels = ['Human Resources', 'Operations', 'Marketing', 'Sales', 'Information Technology', 'Research and Development', 'Finance']
data = [25, 20, 15, 15, 10, 10, 5]
line_labels = ['Allocation (%)']

# Create a dataframe for visualization
import pandas as pd
df = pd.DataFrame(list(zip(data_labels, data)), columns=['Department', 'Allocation'])

# Create the treemap
fig = px.treemap(df, path=['Department'], values='Allocation', 
                 title='Percentage Allocation of Human Resources Across Different Departments',
                 color='Allocation')

# Automatically adjust text in case it is too long
for trace in fig.data:
    trace.textinfo = 'label+value+percent entry'

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/110.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
fig.write_image(save_path)

# Clear the current image state
fig.data = []
