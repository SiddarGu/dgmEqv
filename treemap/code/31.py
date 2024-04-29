import plotly.express as px
import plotly.graph_objects as go
import os

# Prepare the data
data_labels = ['Engagement Score (%)']
line_labels = ['Administration', 'Sales', 'Human Resources', 'Development', 'Marketing', 'Operations', 'Customer Service']
data = [18, 16, 15, 14, 13, 12, 12]

# Create a dataframe
import pandas as pd
df = pd.DataFrame(list(zip(line_labels, data)), columns=['Department', 'Engagement Score'])

# Create the treemap
fig = px.treemap(df, path=['Department'], values='Engagement Score', title='Employee Engagement Scores by Department in Human Resources Management')

# Customize the layout
fig.update_layout(
    margin=dict(l=10, r=10, t=50, b=10)
)

# Save the figure
save_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(save_dir, exist_ok=True)
fig.write_image(os.path.join(save_dir, "31.png"))

# Show figure
fig.show()
