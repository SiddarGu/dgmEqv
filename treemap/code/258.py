import plotly.express as px
import os

# Data preparation
data_labels = ['Revenue Share (%)']
line_labels = ['Hotels', 'Resorts', 'Vacation Rentals', 'Hostels', 'Bed & Breakfasts', 'Motels']
data = [40, 20, 15, 10, 8, 7]

# Transform data into the structure suitable for plotly treemap
categories = {'Accommodation Type': line_labels, 'Revenue Share': data}

# Initialize the figure with Plotly Express
fig = px.treemap(
    categories,
    path=['Accommodation Type'],
    values='Revenue Share',
    title='Revenue Distribution in the Tourism and Hospitality Industry by Accommodation Type'
)

# You can customize your figure as you want here
# e.g., colors, rounded corners, etc.
fig.update_traces(textinfo='label+value', textfont_size=20, marker=dict(line_width=2))

# File path to save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
filename = '1036.png'

# If directory does not exist, create it
os.makedirs(save_path, exist_ok=True)

# Save the figure
fig.write_image(os.path.join(save_path, filename))

# Clear current figure (though in Plotly, this is not typically required as in matplotlib)
fig = None
