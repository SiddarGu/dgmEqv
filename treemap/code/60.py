import plotly.express as px
import os

# Data preparation
data_labels = ["Funding Source (%)"]
line_labels = ["Health Services", "Educational Programs", "Environmental Causes", "Disaster Relief", "Human Rights", "Arts and Culture", "Animal Welfare", "Research and Development"]
data = [22, 18, 15, 13, 12, 10, 5, 5]

# Creating the parent path if it doesn't exist
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png"
os.makedirs(save_path, exist_ok=True)

# Combine the data into one dataframe-like structure for Plotly
full_data = {
    'labels': line_labels,
    'values': data
}

# Create the treemap
fig = px.treemap(
    full_data,
    path=['labels'],
    values='values',
    title='Funding Sources Distribution Among Charity Sectors',
    color='values'
)

# Update layout for aesthetics
fig.update_layout(
    margin = dict(t=50, l=25, r=25, b=25)
)

# Save the figure
fig.write_image(f"{save_path}/60.png")
