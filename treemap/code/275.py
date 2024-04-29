import plotly.express as px
import os

# Creating the data structure
data_labels = ['Fast Food', 'Casual Dining', 'Fine Dining', 'Beverage Manufacturers', 
               'Confectionery', 'Snack Food', 'Organic Food', 'Food Processing', 'Specialty Food']
data = [30, 20, 15, 10, 10, 5, 5, 3, 2]
line_labels = ['Revenue Share (%)']

# Combining the data into a single list of dictionaries for Plotly
data_dict = [{"Category": label, "Revenue Share": value} for label, value in zip(data_labels, data)]

# Create a treemap using Plotly Express
fig = px.treemap(data_dict, path=['Category'], values='Revenue Share',
                 title='Market Revenue Shares within the Food and Beverage Industry')

# Tune the treemap's appearance
fig.update_traces(textinfo="label+percent entry")
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25), font=dict(size=14))

# Define the save path and create directories if they do not exist
save_dir = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(save_dir, exist_ok=True)
save_path = os.path.join(save_dir, "1032.png")

# Save the figure
fig.write_image(save_path)

# This line assumes that you want to clear the figure after saving it to prevent it from being displayed in an interactive session
fig = None
