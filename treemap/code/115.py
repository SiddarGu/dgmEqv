import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Revenue Share (%)']
line_labels = [
    'Online Retailers', 'Physical Stores', 'Electronic Appliances',
    'Fashion and Apparel', 'Groceries', 'Home Furnishings',
    'Health and Beauty Products', 'Books and Music'
]
data = [35, 30, 10, 10, 5, 5, 3, 2]

# Set colors for different sections in the treemap
colors = ['#0f7216', '#b2790c', '#ffe9a3', '#f9d4d4', '#d35158', '#ea3033', '#120c0c', '#fcde9c']

# Create figure
fig = plt.figure(figsize=(12, 8))

# Create a treemap
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7, text_kwargs={'fontsize':9, 'wrap':True})

# Set the title of the figure
plt.title('Revenue Distribution in Retail and E-commerce 2023', fontsize=16)

# Eliminate axis lines
plt.axis('off')

# Use tight layout to automatically adjust subplot params for good figsize
plt.tight_layout()

# Set absolute file path for saving the image
file_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/115.png'

# Save the figure
plt.savefig(file_path, bbox_inches='tight')  # bbox_inches='tight' is used for making sure the labels fit into the image

# Clear the current figure's state after saving
plt.clf()

# Close the plt object to prevent any further changes.
plt.close()
