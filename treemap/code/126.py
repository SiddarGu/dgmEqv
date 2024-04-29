import plotly.express as px
import os

# Given raw data in a single string
raw_data = """Social Media Platform,Web Traffic Share (%)
Facebook,25
YouTube,20
WhatsApp,15
Instagram,10
Twitter,10
Snapchat,7
LinkedIn,5
Pinterest,4
Reddit,2
TikTok,2"""

# Process the data into usable format
lines = raw_data.strip().split('\n')
data_labels = lines[0].split(',')[1:]  # ['Web Traffic Share (%)']
line_labels, data = zip(*[line.split(',') for line in lines[1:]])

# Create lists for labels and sizes
labels = [label for label in line_labels]
sizes = [float(value) for value in data]

# Data for the treemap
treemap_data = {
    'labels': labels,
    'sizes': sizes,
    'parents': ['' for _ in labels]  # No parent as this is the first level
}

# Create a treemap using Plotly
fig = px.treemap(
    treemap_data,
    path=['labels'],
    values='sizes',
    title='Web Traffic Distribution Among Social Media Platforms'
)

# Customize treemap
fig.update_traces(textfont_size=12, textinfo='label+percent entry')

# Create necessary directories for saving the file
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/126.png"
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
fig.write_image(save_path)

# Clear the figure (if using matplotlib, in Plotly this is not required)
# plt.clf()

# The code is complete; no need to close the plot or clear current image state for Plotly
