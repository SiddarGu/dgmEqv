import plotly.express as px
import os

# Given data
data_labels = ['Revenue Share (%)']
line_labels = ['Accommodation', 'Food Services', 'Recreation & Entertainment', 
               'Travel Agent Services', 'Airline Services', 'Transportation Rentals', 
               'Tourism Marketing and Promotion', 'Event Planning']
data = [35, 25, 15, 10, 9, 3, 2, 1]

# Transforming the data into a format suitable for Plotly's treemap function
df = {
    'Category': line_labels,
    'Revenue Share (%)': data
}

fig = px.treemap(df, path=['Category'], values='Revenue Share (%)', title='Revenue Distribution in the Tourism and Hospitality Industry')

# This will ensure that the text doesn't get squeezed or overlapped
fig.update_traces(textinfo="label+percent entry", textfont_size=12)

# Customizations to make the chart fancy
fig.update_layout(
    treemapcolorway=["#003f5c", "#58508d", "#bc5090", "#ff6361", "#ffa600"],
    margin=dict(t=50, l=25, r=25, b=25),
)

# Create the directories if they do not exist
image_dir = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png'
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# Full path for the saved image
image_path = os.path.join(image_dir, '211.png')

# Save the figure
fig.write_image(image_path)

# There is no explicit "clear the current image state" in plotly, as each figure is an independent object
